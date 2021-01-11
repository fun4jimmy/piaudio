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


def make_app():
    """Flask application factory function."""
    application = connexion.FlaskApp(__name__, specification_dir='openapi')
    application.app.json_encoder = JSONEncoder

    application.add_api('openapi.json', arguments={'title': 'piaudio'}, pythonic_params=True)

    api.add_service(AlsaloopService())
    api.add_service(PlexampService())

    flask_application = application.app

    asset_environment = Environment(flask_application)

    javascript_bundle = Bundle('javascript/api.js', filters='jsmin', output='bundles/packed.js')
    asset_environment.register('javascript_bundle', javascript_bundle)

    asset_environment.config['LIBSASS_STYLE'] = 'compressed'

    css_bundle = Bundle('sass/main.scss', filters='libsass', output='bundles/packed.css')
    asset_environment.register('css_bundle', css_bundle)

    # we use blueprints, rather than define the routes within this function, to keep the code more modular
    flask_application.register_blueprint(index)

    return flask_application
