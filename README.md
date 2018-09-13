# Dockerized Flask App

With one bash script you can initialize a 3 container setup as specified in `docker-compose.yml`. From there you can
configure the application to be a API, Full-Stack Framework, or really anything you want it to be. 

_Note: Hot reload on has not been configured for this application yet._ 

## Getting Started

Run the `docker_init.sh` in your project directory

```
$ bash docker_init.sh
```
and and navigate to http://localhost:8080 and you should see the 
welcome text **Time to get building!** which means you're set up! That's it!

## Database Configuration

When you started the containers `Flask-Migrate` updated the database schema with a generic users table setup
that's included in `models.py`. When you initially run the container `Flask-Migrate` will check to see if the 
models in `models.py` match what's currently in your database. In the case of running the container for the first time
, `Flask-Migrate` will create a migration script and create your database for you. Here is what the schema
looks like on when you first start the app. 



![PostgreSQL Schema](http://url/to/img.png)


_Note: Since the database was created through Flask-Migrate you must use Flask-Migrate to continue to alter and update the database moving forward._ 



## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Joseph Haddad** - *Initial work*


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


Links
-----

* Website: https://www.palletsprojects.com/p/flask/
* Documentation: http://flask.pocoo.org/docs/
* License: `BSD <https://github.com/pallets/flask/blob/master/LICENSE>`_
* Releases: https://pypi.org/project/Flask/
* Code: https://github.com/pallets/flask
* Issue tracker: https://github.com/pallets/flask/issues
* Test status:

  * Linux, Mac: https://travis-ci.org/pallets/flask
  * Windows: https://ci.appveyor.com/project/pallets/flask

* Test coverage: https://codecov.io/gh/pallets/flask

.. _WSGI: https://wsgi.readthedocs.io
.. _Werkzeug: https://www.palletsprojects.com/p/werkzeug/
.. _Jinja: https://www.palletsprojects.com/p/jinja/
.. _pip: https://pip.pypa.io/en/stable/quickstart/

