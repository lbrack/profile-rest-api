.. include:: ./links.rst

.. _django-models:

Models
******

documentation: `models documentation`_

The Django Model is an ORM (Object Relational Mapping) allowing to create a bridge
between OO program and relation databases. As such, models are DB agnostic.

Thus, a Python class deriving from :external+django:py:class:`django.db.models.Model` automatically translate to a
DB Table.

When the model changes, Django provides a mechanism to create migrations to update the
DB backend to migrate to the new model definition.

As mentioned, models are DB agnostic.
