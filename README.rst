piaudio
=======

**piaudio** is a web application designed to run on a **Raspberry Pi**, allowing the control of audio services via a web frontend. This allows the **Raspberry Pi** to be controlled via a web browser on a phone, instead of remoting on to the device and stopping and starting the various services via the command line.

Under the hood it uses **Flask_** for serving the web pages and **Connexions_** for providing the REST api that controls the audio services.

Supported Audio Services
------------------------

- **Plexamp_** - For streaming music and audio from a Plex server. This also supports music being casted to the Raspberry Pi from other Plex clients.
- **alsaloop_** - For forwarding the Raspberry Pi auxillary input to the audio output. This allows the Raspberry Pi to act as a pass through audio device.

Requirements
------------

- **Raspberry Pi** or similar **Unix** device.
- **Python 3.8** (may work with earlier versions).
- **alsaloop**.
- **Plexamp** (See the **Plex** forums_ for instructions on installing **Plexamp for Raspberry Pi v.20 beta 2** as a service).

Installation
------------

.. code-block::

    pip install https://github.com/fun4jimmy/piaudio


.. _Flask: https://flask.palletsprojects.com/
.. _Connexions: https://flask.palletsprojects.com/
.. _Plexamp: https://plexamp.com/
.. _alsaloop: https://manpages.debian.org/testing/alsa-utils/alsaloop.1.en.html
.. _forums: https://forums.plex.tv/t/plexamp-for-raspberry-pi-release-notes/368282
