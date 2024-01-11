#!/usr/bin/python3
"""fabric script that generates an archive"""
from fabric.operations import local
import os
from datetime import datetime


def do_pack():
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{time}.tgz"
    source = "web_static"
    os.makedirs(destination, exist_ok=True)
    destination = "versions"
    run = local(f'tar -czvf {destination}/{archive_name} {source}')
    if run.failed:
        return None
    else:
        return os.path.join(destination, archive_name)
