"""Defines a custom JSON encoder for converting api types to JSON."""
from connexion.apps.flask_app import FlaskJSONEncoder

from piaudio.services import BaseService
from piaudio.services import ServiceState


class JSONEncoder(FlaskJSONEncoder):
    """A JSON encoder that is aware of all api types."""

    def default(self, o):
        """Override of FlaskJSONEncoder.default that can also encode our api types."""
        if isinstance(o, ServiceState):
            return o.value

        if isinstance(o, BaseService):
            return o.to_json_dict()

        return super().default(o)
