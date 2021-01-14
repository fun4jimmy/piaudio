"""Stub setup.py as pip does not yet support installing directly from a setup.cfg file."""
import sys

from distutils.version import StrictVersion

from setuptools import __version__ as setuptools_version
from setuptools import setup

# The way we handle reading the version number from __init__.py without requiring
# any package imports to be installed requires a certain version of setuptools.
MINIMUM_SETUPTOOLS_VERSION = '46.4.0'

if StrictVersion(setuptools_version) < StrictVersion(MINIMUM_SETUPTOOLS_VERSION):
    print('Expected setuptools version {} or higher, got version {}.'.format(MINIMUM_SETUPTOOLS_VERSION, setuptools_version))
    sys.exit(1)

setup()
