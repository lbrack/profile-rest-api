.. _profile-api-model:

Profile Models
**************

.. thumbnail:: ./images/models.png

The customized user is implemented as :py:class:`profile_api.models.UserProfile`. It derives
from the following classes:

* :external+django:py:class:`django.contrib.auth.models.AbstractBaseUser`
* :external+django:py:class:`django.contrib.auth.models.PermissionsMixin`

For information on customizing the authentication, check :external+django:doc:`topics/auth/customizing`.
For starter, Django supports a list of authentication backend. When a user attempts to login, all
backend are tried until one succeeds. By default, Django uses the
:external+django:py:class:`django.contrib.auth.backends.ModelBackend`.


To understand the default authentication, check :external+django:doc:`topics/auth/default`.

.. todo:: Check `Jazzband <https://github.com/jazzband/django-two-factor-auth>`_ to enable to factor authentication.

.. todo:: There is the question of how to distinguish between an Employee and a Customer.
          `Here is a pointer <https://stackoverflow.com/questions/72492218/django-user-model-employee-and-customer>`_
          What we want to do is to tie the employee to an organization.

          potential candidate:

          * `django organizations <https://django-organizations.readthedocs.io/en/latest/reference/backends.html>`_