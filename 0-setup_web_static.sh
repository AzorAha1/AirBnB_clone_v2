#!/usr/bin/env bash
# sets up web servers for the deployment of web_static

source=/data/web_static/releases/test/
symlink=/data/web_static/current
configcode="    location /hbnb_static {\n\talias /data/web_static/current/;\n\tindex index.html;\n\t}"
configfile=/etc/nginx/sites-enabled/default
htmlcontent="
<html>
    <body>
        Holberton School
    </body>
</html>
"
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "$htmlcontent" | sudo tee -a "$source/index.html"
if [ -e "$symlink" ]; then
    sudo rm "$symlink"
fi
sudo ln -s $source $symlink
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/server {/a $configcode" "$configfile"
sudo service nginx restart
