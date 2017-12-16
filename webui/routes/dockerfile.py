""" General route """
from flask import render_template, Blueprint
import docker


view = Blueprint('dockerfile', __name__)


@view.route('/dockerfile', methods=['GET'])
def dashboard():
    """ Index page """
    client = docker.from_env()
    plh = \
"""
FROM ubuntu:14.04
MAINTAINER Alexander Telkov <alx9110@yandex.ru>
RUN apt-get update
RUN apt-get install -y nginx
RUN echo 'Hi, I am in your container'
        >/usr/share/nginx/html/index.html
EXPOSE 80
"""
    return render_template('dockerfile.html', plh=plh.strip())