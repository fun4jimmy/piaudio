"""Defines the alsaloop service class."""

from piaudio.services.base import BaseService
from piaudio.services.base import ServiceState
from piaudio.utilities import run_process


class AlsaloopService(BaseService):
    """Alsaloop service which forwards the auxilary audio input directly to the audio output."""

    def __init__(self):
        super().__init__("alsaloop")
        self.playback_device = "dmixer"
        self.playback_rate = 48000
        self.latency_usec = 10000
        # 0 means no sync
        self.sync_mode = 0
        # process wake timeout
        self.wake_timeout = 999999

    def state(self):
        """Return the state of the service."""
        arguments = ['pgrep', 'alsaloop']
        returncode = run_process(arguments)

        if returncode == 0:
            return ServiceState.ACTIVE

        # todo: check logs for alsaloop failure
        return ServiceState.INACTIVE

    def set_state(self, new_state):
        """Set the state of the service."""
        assert isinstance(new_state, ServiceState)

        if new_state not in [ServiceState.ACTIVE, ServiceState.INACTIVE]:
            raise ValueError("Call to set_state for service {} failed : invalid state {}.".format(self.id, new_state))

        current_state = self.state()
        if new_state == current_state:
            return True

        if new_state == ServiceState.ACTIVE:
            arguments = [
                'alsaloop',
                '--daemonize',
                '--pdevice={}'.format(self.playback_device),
                '--rate={}'.format(self.playback_rate),
                '--tlatency={}'.format(self.latency_usec),
                '--sync={}'.format(self.sync_mode),
                '--wake={}'.format(self.wake_timeout),
                ]
            return run_process(arguments) == 0

        arguments = ['pkill', 'alsaloop']
        return run_process(arguments) == 0
