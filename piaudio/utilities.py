"""A collection of useful utility functions."""
import shlex
import subprocess

from flask import current_app


def run_process(arguments):
    """Execute a command on the host system returning the result."""
    try:
        current_app.logger.debug("Running command '%s'.", shlex.join(arguments))
        process = subprocess.run(arguments, check=False)
        return process.returncode
    except FileNotFoundError:
        current_app.logger.error("Command '%s' failed: file not found.", shlex.join(arguments))
        return -1
