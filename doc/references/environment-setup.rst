.. include:: ./links.rst

.. _environment-setup:

Environment Setup
*****************

This chapter assumes that you do not have PDM, vagrant and virtual box installed on your machine.

Installing PDM
==============

following the instructions provided on `the PDM main documentation <https://pdm.fming.dev/latest/#installation>`_

Installing Vagrant && Virtual Box
=================================

While it is possible to install both via the command line, the easiest is to install both
vagrant and virtual box via the software manager provided with your linux distribution.

.. _vagrant_provisioning:

Vagrant Provisioning
====================

Setting up vagrant the first time
---------------------------------

To initialize the vagrant file the first time, you run the following command and then fill out
the vagrant file (below)

.. code-block:: shell

    ❯ vagrant init ubuntu/bionic64
    A `Vagrantfile` has been placed in this directory. You are now                                                                                                                                                                   ─╯
    ready to `vagrant up` your first virtual environment! Please read
    the comments in the Vagrantfile as well as documentation on
    `vagrantup.com` for more information on using Vagrant.
    ╭─ ~/github/lbrack/profile-rest-api ··················· ✔  profile-rest-api Py ─╮
    ╰─                                                                             ─╯

Vagrant File
------------

Below is the vagrant file found in the root directory. This file is used to provision the vagrant
boxes. Because the project uses PDM and PDM relies on Python 3.7 or higher, we have to install Python
(at the time of writing, 3.8 was available).

.. literalinclude:: ../../Vagrantfile
   :language: ruby
   :emphasize-lines: 13,23-29,32-37, 39-40
   :linenos:

On line **13** forward the port from the host OS to the guest one so the app can be
reached from the dev machine.

on line **22**, we install python 3.8 and alias python with that version thus overriding
the default python executable.

On line **31** we install PDM (as vagrant and not root), set the path and execute some
useful aliases to start the server.

On line **39**, we create a virtual environment (called *vagrant*) using PDM and use it
by default in this project. This environment is created in another location so it doesn't
interfere with the ``.venv`` dev environment at the root of the project. Finally, we set
the environment as the default on that vagrant box.

Finally, on line **40**, we run PDM install to install all the dependencies so we can run
our server.

.. code-block:: shell

    $ vagrant destroy -gf # Destroy the vagrant boc
    $ vagrant up # start the vagrant box
    $ vagtant up --provision # start the box and run the shell command on line 16
    $ vagrant ssh # ssh to the vagrant box.
