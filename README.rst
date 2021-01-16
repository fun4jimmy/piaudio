=======
piaudio
=======

piaudio is a web application designed to run on a Raspberry Pi, allowing the control of audio services via a web frontend. This allows the Raspberry Pi to be controlled via a web browser on a phone, instead of remoting on to the device and stopping and starting the various services via the command line.

Under the hood it uses Flask_ for serving the web pages and Connexions_ for providing the REST api that controls the audio services.

Supported Audio Services
========================

- Plexamp_ - For streaming music and audio from a Plex server. This also supports music being casted to the Raspberry Pi from other Plex clients.
- alsaloop_ - For forwarding the Raspberry Pi auxillary input to the audio output. This allows the Raspberry Pi to act as a pass through audio device.

Requirements
============

- Raspberry Pi or similar Unix device.
- Python 3.8 (may work with earlier versions).
- alsaloop.
- Plexamp (See the Plex forums_ for instructions on installing Plexamp for Raspberry Pi v.20 beta 2 as a service).

Installation
============

- Install the requirements for a nginx server and a Python virtual environment for the application.

  .. code-block::

      sudo apt update
      sudo apt install python3 python3-venv
      sudo apt install uwsgi uwsgi-plugin-python3
      sudo apt install nginx

- Setup a Python virtual environment.

  .. code-block::

      mkdir piaudio
      cd piaudio
      python3 -m venv venv
      venv/bin/pip install --upgrade pip

- Install the application in the new virtual environment (note: piaudio requires setuptools 46.4.0 or later).

  .. code-block::

      venv/bin/pip install --upgrade setuptools
      venv/bin/pip install https://github.com/fun4jimmy/piaudio/archive/main.tar.gz

  To install a specific version change the github link to refer to one of the release bundles eg. https://github.com/fun4jimmy/piaudio/archive/v1.0.0.tar.gz.

- Create an ini file (eg. piaudio.ini) for the uwsgi configuration.

  .. code-block::

    [uwsgi]
    # Set the require the uwsgi plugin
    plugin = python3
    # the application factory function (make_app) within our application package (piaudio)
    module = piaudio:make_app()
    # the relative path to our virtual environment (working directory is set in the service config)
    virtualenv = venv

    # there aren't any other uwsgi processes so we are the master.
    master = true
    # we're not expecting many concurrent requests so limit uswgi to a single process
    processes = 1

    # name the socket for communication with nginx
    socket = piaudio.sock
    # make sure the group owner nginx can read and write to the socket.
    chmod-socket = 660
    # clean up the socket on exit
    vacuum = true

    # relative path to the uwsgi log (working directory is set in the service config)
    daemonize = uwsgi.log

    die-on-term = true

- Add a service for the application uwsgi instance so it will automatically start with the Raspberry Pi.

  **/etc/systemd/system/piaudio.service:**

  .. code-block::

    [Unit]
    Description=uWSGI instance to serve piaudio
    After=network.target

    [Service]
    User=<username>
    Group=www-data
    # all paths in piaudio.ini are relative to this directory
    WorkingDirectory=/home/<username>/piaudio
    ExecStart=/usr/bin/uwsgi --ini piaudio.ini

    [Install]
    WantedBy=multi-user.target

- Add a nginx site definition for the application.

  **/etc/nginx/sites-available/piaudio:**

  .. code-block::

    server {
      listen 80;
      server_name piaudio;

      location / {
        include uwsgi_params;
        uwsgi_pass unix:///home/<username>/piaudio/piaudio.sock;
      }
    }

- Add the nginx site to the list of enable sites, test the definition is ok and restart nginx.

  .. code-block::

    sudo ln -s /etc/nginx/sites-available/piaudio /etc/nginx/sites-enabled
    sudo nginx -t
    sudo systemctl restart nginx


.. _Flask: https://flask.palletsprojects.com/
.. _Connexions: https://flask.palletsprojects.com/
.. _Plexamp: https://plexamp.com/
.. _alsaloop: https://manpages.debian.org/testing/alsa-utils/alsaloop.1.en.html
.. _forums: https://forums.plex.tv/t/plexamp-for-raspberry-pi-release-notes/368282
