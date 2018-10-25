
pqbackup
========

CLI for backing up remote PostgreSQL database locally or to an AWS S3 bucket.

Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone the repository ``https://github.com/shazic/pgbackup``
3. Fetch development dependencies: ``make install``

Usage
-----

Pass in a full database url, storage driver and destination.

S3 example with bucket name:

::

    $ pgbackup postgres://user@example.com:5432/db_name --driver s3 my_bucket_name

Local example with file name:

::

    $ pgbackup postgres://user@example.com:5432/db_name --driver local /var/local/db_name/backups/dump_2018_09_30.sql

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenvisn't active, use:

::

    $ pipenv run make

