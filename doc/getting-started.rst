.. _getting-started:

Getting Started
***************

.. contents::

There is a minimalistic setup required. The following instructions are for Linux but should
be fairly similar for OSX.

First clone the `project <https://github.com/lbrack/profile-rest-api>`_ and then proceed to
the :ref:`environment-setup`.

Install Graphviz (used for DB model rendering)

.. code-block:: shell

    ❯ sudo apt install graphviz # Graphiz executables and libraries
    ❯ sudo apt install graphviz-dev # headers to compile the python extension

This should allow for the installation of pygraphviz which will be needed for the
`dhango-extensions <https://django-extensions.readthedocs.io/en/latest/index.html>`_

.. code-block:: shell

    ❯ pdm add -dG django pygraphviz
    Adding packages to django dev-dependencies: pygraphviz
    🔒 Lock successful
    Changes are written to pyproject.toml.
      ✔ Install pygraphviz 1.11 successful
    🎉 All complete!


Once PDM, Vagrant and VirtualBox are installed, you can test the tires by doing the following:

* **[host]** install the project dependencies

.. code-block:: shell

    ❯ pdm install

* **[host]** fire up and provision the vagrant box.

.. code-block:: shell

    ❯ vagrant up
    Bringing machine 'default' up with 'virtualbox' provider...                                                                                                                                                                      ─╯
    ==> default: Importing base box 'ubuntu/bionic64'...
    ==> default: Matching MAC address for NAT networking...
    ==> default: Checking if box 'ubuntu/bionic64' version '20200304.0.0' is up to date...
    ...
    ==> default: Forwarding ports...
        default: 8000 (guest) => 8000 (host) (adapter 1)
        default: 22 (guest) => 2222 (host) (adapter 1)
    ==> default: Running 'pre-boot' VM customizations...
    ==> default: Booting VM...
    ==> default: Waiting for machine to boot. This may take a few minutes...
        default: SSH address: 127.0.0.1:2222
        default: SSH username: vagrant
        default: SSH auth method: private key
    ...
    default: Successfully installed: PDM (2.8.2) at /home/vagrant/.local/bin/pdm
    default: Post-install: Please add /home/vagrant/.local/bin to PATH by executing:
    default:     export PATH=/home/vagrant/.local/bin:$PATH
    ...
    default: Virtualenv /home/vagrant/.local/share/pdm/venvs/vagrant-atX9vL8u-vagrant is created successfully
    default: Using Python interpreter: /home/vagrant/.local/share/pdm/venvs/vagrant-atX9vL8u-vagrant/bin/python (3.8)
    ...
    default:   ✔ Install zipp 3.6.0 successful
    default:
    default: 🎉 All complete!
    default:
    ❯
    ╭─ ~/github/lbrack/profile-rest-api  master +10 !10 ······· ✔  profile-rest-api Py ─╮
    ╰─                                                                                 ─╯

* **[host]** Once the machine is provisioned using the :ref:`vagrant configuration <vagrant_provisioning>`, you can ssh to the box

.. code-block:: shell

    ❯ vagrant ssh
    Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 4.15.0-212-generic x86_64)
    ...
    Last login: Sat Aug 26 16:47:56 2023 from 10.0.2.2
    VAGRANT SERVER ubuntu-bionic
    vagrant@ubuntu-bionic:/vagrant$ pdm --version
    PDM, version 2.8.2

* **[guest]** and then start the server

.. code-block:: shell

    vagrant@ubuntu-bionic:/vagrant$ runserver
    RUNNING ON ubuntu-bionic
    Virtualenv /home/vagrant/.local/share/pdm/venvs/vagrant-atX9vL8u-vagrant is reused.
    /vagrant/src /vagrant
    Watching for file changes with StatReloader
    Performing system checks...

.. _aliases:

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

Superuser Creation
==================

❯ manage createsuperuser
Email: laurent.brack@protonmail.com
Name: lbrack
Password:
Password (again):
Superuser created successfully.

.. note:: My password is "moi a mon annee de naissance"

Migrations
==========

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

Dealing with Models
===================

The general principle is that you create an application, at the same level as the server.
You create the model for that application in the models file (I think you can make it a package).
And finally, in the admin.py. you register the model with Django

.. note:: I am assuming here that the server could have different databases.

Building Documentation
======================

The documentation is built using Sphinx and ReST. It is built on every git push using
red the docs (https://readthedocs.org/projects/profile-rest-api/) and the documentation
is visible at https://profile-rest-api.readthedocs.io/en/latest/.

In order to cross reference Django documentation, interpshinx is being used. There is however
a bug which prevents us from refering to the inventory url directly. Instead, the inventory file
is downloaded offline and stored in the repos under the ``doc/django.inv``. The current documentation
is built against Django 4.2 (which is set in the make file).

Unless we change the django documentation, we do not need to update the inventory file. However,
if this is needed, one need to set the new version in the make file and call ``make django-ref``.
In addition to downloading the inventory file, this target will also display the content of the
inventory.

example:

.. code-block:: shell

    ❯ make django-ref
    ...
    translation string                       topics/i18n/#term-translation-string
    view                                     glossary/#term-view
    content of doc/django.inv version 4.2 - see doc/conf.py for details

to build the documentation, type:

.. code-block:: shell

    ❯ make doc
    # or to open the doc in the browser
    ❯ make open

.. seealso:: :ref:`doc-cheat-sheet` for documentation tricks

