.. include:: ./links.rst

.. _getting-started:

Getting Started
***************

Aliases
-------

you can source the ``.aliases`` file on either the local host or vagrant
box.

* ``pyrun``

  a short for ``pdm run``

* ``pyroot``

  changes the directory to the project root using ``pdm info --where``

* ``runserver``

  this alias can be run on the host or vagrant box and will start the
  django server on ``0.0.0.0:8000``

Migrations
----------

Whenever the model is changed, a migration shall be created. To create a
migration, type:

.. code-block:: shell

    ❯ manage makemigrations profile_api
    Migrations for 'profile_api':
      profile_api/migrations/0001_initial.py
        - Create model UserProfile

This will create a migration file as shown above (which should be checked in).
To apply the migration, type

.. code-block:: shell

    ❯ manage migrate
    ~/github/lbrack/profile-rest-api/src ~/github/lbrack/profile-rest-api                                                                                                                                                            ─╯
    Operations to perform:
      Apply all migrations: admin, auth, authtoken, contenttypes, profile_api, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      ...
      Applying sessions.0001_initial... OK

