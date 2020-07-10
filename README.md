# Django Auth App

Very basic Django authentication application.

## Installation

```bash
pipenv shell
pipenv install
py ./manage.py migrate
py ./manage.py createsuperuser
py ./manage.py collectstatic
py ./manage.py runserver
open: http://localhost:8000/
```

## Description

A basic Django app to demonstrate authentication features offered by Django.
Can be used if you coding entire page in Django.
If you using Django just for back-end, I'd use API / JWT based authentication (with REST or GraphQL).

Following features are available:

-   Register user
-   Login
-   Logout
-   Edit user profile
-   Edit password

## Author

[James La Guma](https://www.linkedin.com/in/jlaguma/)
