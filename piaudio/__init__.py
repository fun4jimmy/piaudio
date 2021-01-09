"""Flask site application factory for switching between audio applications on the host system."""
from flask import render_template

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
    # we use blueprints, rather than define the routes within this function, to keep the code more modular
    flask_application.register_blueprint(index)

    return flask_application
