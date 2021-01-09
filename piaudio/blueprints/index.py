"""Module for the index page blueprint."""
from flask import Blueprint
from flask import render_template

index = Blueprint('index', __name__)


@index.route('/')
def render():
    """Render the index page static template."""
    return render_template('index.html')
