"""Defines the plexamp service class."""

from piaudio.services.base import BaseService
from piaudio.services.base import ServiceState
from piaudio.utilities import run_process


class PlexampService(BaseService):
    """Plexamp service which manages the plexamp service that streams Plex server audio."""

    def __init__(self):
        super().__init__("plexamp")

    def state(self):
        """Return the state of the service."""
        arguments = ['systemctl', 'is-active', '--quiet', 'plexamp']
        returncode = run_process(arguments)

        if returncode == 0:
            return ServiceState.ACTIVE

        # todo: query the Plexamp service for failure
        return ServiceState.INACTIVE

    def set_state(self, new_state):
        """Set the state of the service."""
        assert isinstance(new_state, ServiceState)

        if new_state not in [ServiceState.ACTIVE, ServiceState.INACTIVE]:
            raise ValueError("Call to set_state for service {} failed : invalid state {}.".format(self.id, new_state))

        current_state = self.state()
        if new_state == current_state:
            return True

        operation = "start" if new_state == ServiceState.ACTIVE else "stop"

        arguments = ['sudo', 'systemctl', operation, 'plexamp']
        return run_process(arguments) == 0
