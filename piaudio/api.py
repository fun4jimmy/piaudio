"""Module for all site api route handling."""
from flask import current_app

from piaudio.services import BaseService
from piaudio.services import ServiceState


_services = []


def add_service(service):
    """Add a new service to the list of services."""
    assert isinstance(service, BaseService)

    if find_service(service.id) is not None:
        raise ValueError("A service with id '{}' has already been added.".format(service.id))

    _services.append(service)


def find_service(service_id):
    """Find a service in the list of services."""
    for service in _services:
        if service.id == service_id:
            return service

    return None


def list_services():
    """List all services supported by the piaudio host."""
    return _services


def get_service(service_id):
    """Return the requested service object."""
    requested_service = find_service(service_id)

    if requested_service is None:
        return "Service {} not found.".format(service_id), 404

    return requested_service, 200


def set_service(service_id, state):
    """Set the state of the requested service object."""
    requested_service = find_service(service_id)
    # Convert to an instance of ServiceState.
    # This also checks for valid values and raises an error if no match is found.
    state = ServiceState.from_value(state)

    if requested_service is None:
        return "Service {} not found.".format(service_id), 404

    if state == ServiceState.ACTIVE:
        for service in _services:
            if service != requested_service:
                if not service.set_state(ServiceState.INACTIVE):
                    current_app.logger.warning("Failed to set service %s to state %s.", ServiceState.INACTIVE)

    if requested_service.set_state(state):
        return "Audio service state updated", 200

    return "Failed to set the service state", 500
