.. include:: ./links.rst

.. _project-setup:

## setting up workspace

```
pdm init
pdm add -dG test pytest
pdm add -dG dev Ipython
pdm add -dG doc sphinx
pdm add -dG lint  black flake8
```


#### starting the server

```
❯ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...                                                                                                                                                                      ─╯
==> default: Box 'ubuntu/bionic64' could not be found. Attempting to find and install...
    default: Box Provider: virtualbox
    default: Box Version: ~> 20200304.0.0
...
    default: Setting up zip (3.0-11build1) ...
    default: Setting up python3-lib2to3 (3.6.9-1~18.04) ...
    default: Setting up python3-distutils (3.6.9-1~18.04) ...
    default: Setting up python3-venv (3.6.7-1~18.04) ...
    default: Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
    default: Processing triggers for mime-support (3.60ubuntu1) ...
```

The first time around, the machine is provisioned according to the vagrant file. It is however possible to force re-provisioning by invoking

```vagrant up --provision```

### Setting UP PDM on the Vagrant Box

By default, PDM will look at the default .venv folder

```
❯ pdm info
PDM version:
  2.8.2
Python Interpreter:
  /home/lbrack/github/lbrack/profile-rest-api/.venv/bin/python (3.11)
Project Root:
  /home/lbrack/github/lbrack/profile-rest-api
Local Packages:
```

If we use multiple versions of Python between the vagrant box and the host, this could cause conflicts, therefore we want to create a separate virtual environment as shown below.

```
vagrant@ubuntu-bionic:/vagrant$ pdm venv create --force --name vagrant 3.8
Virtualenv /home/vagrant/.local/share/pdm/venvs/vagrant-atX9vL8u-vagrant is created successfully

vagrant@ubuntu-bionic:/vagrant$ pdm venv list
Virtualenvs created with this project:

*  in-project: /vagrant/.venv
-  vagrant: /home/vagrant/.local/share/pdm/venvs/vagrant-atX9vL8u-vagrant

# Set the environment to use
vagrant@ubuntu-bionic:/vagrant$ pdm use --venv vagrant
Using Python interpreter: /home/vagrant/.local/share/pdm/venvs/vagrant-atX9vL8u-vagrant/bin/python (3.8)

vagrant@ubuntu-bionic:/vagrant$ pdm info
The saved Python interpreter doesn't match the project's requirement. Trying to find another one.
Virtualenv /home/vagrant/.local/share/pdm/venvs/vagrant-atX9vL8u-vagrant is reused.
PDM version:
  2.8.2
Python Interpreter:
  /home/vagrant/.local/share/pdm/venvs/vagrant-atX9vL8u-vagrant/bin/python (3.8)
Project Root:
  /vagrant
Local Packages:
```
Now this is the equivalent in the ``.vagrantfile``

```
runuser -l vagrant -c 'export PATH=/home/vagrant/.local/bin:$PATH;cd /vagrant;pdm venv remove --yes vagrant;pdm venv create --force --name vagrant 3.8;pdm use --venv vagrant'
```

## Creating the Django Project

``pdm run django-admin startproject <project name> .``

### Creating an Application

To create a new Django Application
``manage startapp <app name>``

Then edit settings.py in the main project and  type
  ```# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]   "rest_framework", # Add the rest framework
    "rest_framework.authtoken", # add support for Token
    "profile_api" # Finally add our application
