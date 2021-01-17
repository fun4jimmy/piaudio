===================
Changelog (piaudio)
===================

0.0.3 (2021-01-16)
==================

- Add a minimum python version requirement of 3.8 due to use of shlex.join().
- Allow calls to subprocess.run to return non-zero exit codes without raising an exception as this is how some services check if they are currently running.
- Fix the service checkbox handling code so it is not always trying to set the corresponding service to active.
- Fix wake argument to alsaloop activation command line, '--wake=N' is not valid even though the command help text lists it.
- Change the playback device for the alsaloop service to default. The dmixer device was found to consume too much cpu after a long period of running.

0.0.2 (2021-01-14)
==================

- Update setup.py to fail with a helpful message if the wrong version of setuptools is found when installing.
- Fix the name of the Flask-Assets package in the install_requires dependencies.
- Fix the path to the OpenAPI definition in MANIFEST.in so it is included when the package is installed.
- Fix the Sass global-include file pattern in MANIFEST.in so all Sass files are included when the package is installed.
- Add connexion[swagger-ui] package to the install_requires dependencies so the api specification is browsable via http://<site_url>/api/ui/.
- Improve the layout and styling of the application so it can handle a pixel 3 screen in landscape and portrait.

0.0.1 (2021-01-13)
==================

- Initial creation of the piaudio package and the accompanying setuptools configuration.
