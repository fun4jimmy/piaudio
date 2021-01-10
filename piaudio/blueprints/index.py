"""Module for the index page blueprint."""
from flask import Blueprint
from flask import render_template

from piaudio import api

index = Blueprint('index', __name__)


@index.route('/')
def render():
    """Render the index page static template."""
    services = api.list_services()
    return render_template('index.html', services=services)
