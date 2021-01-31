# fikr  
![Django Fikr CI](https://github.com/itzmestar/fikr/workflows/Django%20Fikr%20CI/badge.svg) 
-------
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
-------
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif" border="0" alt="A Django project." title="A Django project." /></a>
-------

Fikr is an Urdu word meaning `to care`.

It's a `django rest framework` based project to host ledger_book app.

Ledger_book app is django app to keep track of financial transaction of a small sized Non Profitable Organization.

## API endpoints

Two API endpoints are implemented:
1. /api/tx/

2. /api/balance/

Only `SessionAuthentication` and `BasicAuthentication` has been enabled.

API endpoint `/api/balance/`  doesn't require authentication.

## check the live demo:

https://ec2-13-126-57-98.ap-south-1.compute.amazonaws.com/api/tx/

https://ec2-13-126-57-98.ap-south-1.compute.amazonaws.com/api/balance/

You can use these credentials to test it out:
```
User: test
Password: 1234test
```
