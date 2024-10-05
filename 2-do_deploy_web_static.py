# 2-do_deploy_web_static.py
from fabric import task
from fabric.connection import Connection
from invoke.exceptions import UnexpectedExit
from os.path import exists

env_hosts = ['54.82.87.226', '34.229.16.34']  # List of your server IPs
env_user = 'ubuntu'
env_key_filename = '~/.ssh/id_rsa'

@task
def do_deploy(c, archive_path):
    """Distribute archive to web servers"""
    if not exists(archive_path):
        print("Archive path does not exist.")
        return False

    try:
        archive_file = archive_path.split("/")[-1]
        no_ext = archive_file.split(".")[0]
        release_folder = f"/data/web_static/releases/{no_ext}/"

        # Upload the archive to the /tmp/ directory on the server
        c.put(archive_path, "/tmp/")

        # Uncompress the archive
        c.run(f"mkdir -p {release_folder}")
        c.run(f"tar -xzf /tmp/{archive_file} -C {release_folder}")
        c.run(f"rm /tmp/{archive_file}")

        # Move the contents from web_static folder to release folder
        c.run(f"mv {release_folder}web_static/* {release_folder}")
        c.run(f"rm -rf {release_folder}web_static")

        # Delete the old symbolic link and create a new one
        c.run("rm -rf /data/web_static/current")
        c.run(f"ln -s {release_folder} /data/web_static/current")

        print("New version deployed successfully!")
        return True

    except UnexpectedExit as e:
        print(f"Deployment failed: {e}")
        return False
