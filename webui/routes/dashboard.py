""" General route """
from flask import render_template, Blueprint
from ..common import docker
import subprocess


view = Blueprint('dashboard', __name__)


@view.route('/', methods=['GET'])
def dashboard():
    """ Index page """
    nets = subprocess.check_output('docker network ls', shell=True).decode().split('\n')[1:]
    nets_obj = [docker.Network(raw) for raw in nets if raw]
    return render_template('base.html', nets=nets_obj)
