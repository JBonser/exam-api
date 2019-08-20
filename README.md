# Exam API

This is an API to allow school teachers to create/administer and score examinations.

This is solely an API and a separate frontend would need to be created that
would use the API to provide a web/mobile or native application user interface.

## Installation

```bash
python3 -m venv env
source env/bin/activate
pip install -e .
```

## Running the Application

### Development

If running for the first time you will need to create the DB, run:

```bash
alembic upgrade head
```

To run the application in development simply call:

```bash
uvicorn app.main:app --reload
```

## Running the Tests

To run the unit tests use the unittest discovery like so:

```bash
pytest tests/
```

### Running with coverage

```bash
pytest --cov=app/ tests/
```

## Updating the database models

If you change any of the database models you will need to ruin alembic to allow it to detect any schema changes,
so that it can try and generate the migration script for you. To do this you need to run:

```bash
alembic revision --autogenerate
```

This will generate a database migration revision which you should then go and inspect to see what migrations have been
generated. This process can sometimes work incorrectly so it's important to check this revision file before comitting.

## Project Spec

Create an application which meets the following requirements:

A teacher of a year 10 math class would like a simple application which gives them the ability to test pupils using multiple choice questions, and also have the ability to determine the pass or fail rate for those that take the tests. The application should allow for pupils to register and take the created test questions, following on from the registration process. Once a pupil has taken the test, that pupil should be notified of whether they have passed or failed. When pupils have taken the tests, the teacher should have the ability to see all pupils and their related test scores, in one single location.

The application should provide the following:

For teachers:

* The ability to add multiple choice questions, of varying difficulties, with 3 possible solutions and potentially multiple possible answers.
* The ability to define a pass/fail percentage for pupils taking the tests
* The ability to view all pupils that have taken the tests and their respective scores

For Pupils:

* The ability to register to take a test, with at least the following details:
  * First Name
  * Surname
  * Email address
* The ability to take a test
* The ability to receive a notification of whether they have passed or failed
