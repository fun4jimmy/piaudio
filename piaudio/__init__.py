"""Flask site application factory for switching between audio applications on the host system."""
import os.path

from flask import render_template
from flask_assets import Environment
from flask_assets import Bundle

import connexion

from piaudio import api
from piaudio.blueprints import index
from piaudio.json_encoder import JSONEncoder
from piaudio.services import AlsaloopService
from piaudio.services import PlexampService


def bundle_javascript(environment):
    """Define and register the bundle for javascript assets."""
    contents = [
        # jQuery library https://jquery.com/
        'javascript/jquery-3.5.1.js',
        # Our own api client
        'javascript/api.js',
        # Our own ui code
        'javascript/ui.js',
    ]
    javascript_bundle = Bundle(*contents, filters='jsmin', output='bundles/packed.js')

    environment.register('javascript_bundle', javascript_bundle)


def bundle_sass(environment):
    """Define and register the bundle for sass assets."""
    # Configure the libsass asset compiler
    environment.config['LIBSASS_STYLE'] = 'compressed'

    contents = [
        # The main stylesheet for the site
        'sass/main.scss',
    ]
    css_bundle = Bundle(*contents, filters='libsass', output='bundles/packed.css')

    environment.register('css_bundle', css_bundle)


def make_app():
    """Flask application factory function."""
    application = connexion.FlaskApp(__name__, specification_dir='openapi')
    application.app.json_encoder = JSONEncoder

    application.add_api('openapi.json', arguments={'title': 'piaudio'}, pythonic_params=True)

    api.add_service(AlsaloopService())
    api.add_service(PlexampService())

    flask_application = application.app

    asset_environment = Environment(flask_application)
    bundle_javascript(asset_environment)
    bundle_sass(asset_environment)

    # we use blueprints, rather than define the routes within this function, to keep the code more modular
    flask_application.register_blueprint(index)

    return flask_application
