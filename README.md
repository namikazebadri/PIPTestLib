# Python Library

This project consists of code for creating minimal python library and deploying it to Pypi.

## Running Unit Test

`pytest`

## Running Code Coverage

`pytest --cov-report html --cov-report term --cov=pylib tests/`

## Running Static Analysis

To run static analysis using flake8, run this command:

`flake8 --config=.flake8 --count --statistics pylib/`