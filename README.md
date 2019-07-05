# Ingresse Dev Test

The purpose of this project is to create an API that manages information of an candidate looking 
for new jobs.  <br>
The candidate has an can apply to multiple companies and receive multiple feedbacks. <br>
The database used for this project is PostgreSQL.

---

[![build-status-badge]][build-status]
[![codecov](https://codecov.io/gh/marcgibbons/django-rest-swagger/branch/master/graph/badge.svg)](https://codecov.io/gh/marcgibbons/django-rest-swagger)
[![pypi-version]][pypi]


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


#### An API documentation generator for thi API

Full documentation: #


## Building

1. `pip install -r requirements.txt`

2. `python manage.py makemigrations` [optional]

3. `python manage.py migrate` [optional]

4. `python manage.py runserver`


## Deploy to Heroku

Run the following commands to deploy the app to Heroku:

```sh
$ git clone https://github.com/lucasrodrigues10/ingresse_dev_test
$ cd ingresse_dev_test
$ heroku create
$ git push heroku master:master
$ heroku open
```

## Requirements
* Django 2.2+
* Django REST framework 3.5.1+
* Python 3.5, 3.6

## Testing

- Run `$ tox` to execute the test suite against all supported environments.
- Run `./runtests.py` to run the test suite within the current environment.

## Bugs & Contributions

Please report bugs by opening an issue

Contributions are welcome and are encouraged!

## License
```
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

[build-status-badge]: https://travis-ci.org/marcgibbons/django-rest-swagger.svg?branch=master
[build-status]: https://travis-ci.org/marcgibbons/django-rest-swagger
[pypi-version]: https://img.shields.io/pypi/v/django-rest-swagger.svg
[pypi]: https://pypi.python.org/pypi/django-rest-swagger
[license]: https://pypi.python.org/pypi/django-rest-swagger/
[docs-badge]: https://readthedocs.io/projects/django-rest-swagger/badge/
[docs]: http://django-rest-swagger.readthedocs.io/