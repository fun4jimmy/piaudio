"""The base interface for all services."""
import enum


class ServiceState(enum.Enum):
    """The enum defining service states."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    FAILED = "failed"


class BaseService(object):
    """The base interface class for all services."""

    def __init__(self, service_id):
        self._id = service_id
        self._name = None

    @property
    def id(self):  # pylint: disable=invalid-name
        """Getter for the service id property."""
        return self._id

    @property
    def name(self):
        """Getter for the service name property."""
        return self._name or self._id

    @name.setter
    def name(self, name):
        """Setter for the service name property."""
        assert name is None or isinstance(name, str)
        self._name = name

    def state(self):
        """Return the state of the service."""
        raise NotImplementedError()

    def set_state(self, new_state):
        """Set the state of the service."""
        raise NotImplementedError()

    def to_json_dict(self):
        """Return the service instance as a dict object suitable for conversion to JSON."""
        json_dict = {
            "id": self._id,
            "state": self.state().value,
        }

        if self._name:
            json_dict["name"] = self._name

        return json_dict
