from fabric import Connection
from invoke import task
from os.path import exists

# Define your hosts and user information
hosts = ['54.82.87.226', '34.229.16.34']
user = 'ubuntu'
key_filename = '~/.ssh/id_rsa'

@task
def do_deploy(c, archive_path):
    """Distributes an archive to the web servers."""
    if not exists(archive_path):
        print("File does not exist!")
        return False

    try:
        archive_file = archive_path.split("/")[-1]
        no_ext = archive_file.split(".")[0]
        release_folder = f"/data/web_static/releases/{no_ext}/"

        for host in hosts:
            conn = Connection(host=host, user=user, connect_kwargs={"key_filename": key_filename})
            
            # Upload the archive to the /tmp/ directory
            conn.put(archive_path, "/tmp/")
            
            # Uncompress the archive to the release folder
            conn.run(f"mkdir -p {release_folder}")
            conn.run(f"tar -xzf /tmp/{archive_file} -C {release_folder}")
            conn.run(f"rm /tmp/{archive_file}")
            
            # Move the web_static contents and set up the symbolic link
            conn.run(f"mv {release_folder}web_static/* {release_folder}")
            conn.run(f"rm -rf {release_folder}web_static")
            conn.run(f"rm -rf /data/web_static/current")
            conn.run(f"ln -s {release_folder} /data/web_static/current")
        
        print("New version deployed successfully!")
        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
