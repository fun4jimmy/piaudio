Changelog (piaudio)
===================

0.0.2 (2021-01-14)

- Update setup.py to fail with a helpful message if the wrong version of setuptools is found when installing.
- Fix the name of the Flask-Assets package in the install_requires dependencies.
- Fix the path to the OpenAPI definition in MANIFEST.in so it is included when the package is installed.
- Fix the Sass global-include file pattern in MANIFEST.in so all Sass files are included when the package is installed.
- Add connexion[swagger-ui] package to the install_requires dependencies so the api specification is browsable via http://<site_url>/api/ui/.

0.0.1 (2021-01-13)
------------------

- Initial creation of the piaudio package and the accompanying setuptools configuration.
