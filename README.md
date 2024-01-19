# fizzbuzz_server

## Introduction

This is a simple Flask-based REST server that implements the Fizz-Buzz logic. It supports both GET and POST requests for generating Fizz-Buzz sequences and provides basic statistics about the most frequently used parameters.

## Build Instructions

There are no special build instructions for this project. You can run the server using the following command:

python fizzbuzz_server.py
Make sure you have Python and the required dependencies installed.

Third-party Libraries
The following third-party libraries are used in this project:

Flask: A lightweight web framework for Python. Used to handle HTTP requests and responses.
Flask-WTF: An extension for Flask that integrates with WTForms, used for input validation.
SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library. Used for database interaction.
Waitress: A production-ready WSGI server. Used to serve the Flask application.

Install these dependencies using the following command:

pip install Flask Flask-WTF SQLAlchemy waitress

API Documentation
The API provides the following endpoints:

GET /: A welcome message.
GET /fizzbuzz: Generate Fizz-Buzz sequences.
POST /fizzbuzz: Generate Fizz-Buzz sequences based on user input.
GET /statistics: Retrieve statistics about the most frequently used parameters.

Example API Usage

POST Request sample:

http POST http://127.0.0.1:5000/fizzbuzz?int1=9&int2=5&limit=150&str1=fizz&str2=buzz

Retrieve Statistics:

http GET http://127.0.0.1:5000/statistics
