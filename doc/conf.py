# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os

project = "Profile Rest API"
copyright = "2023, Laurent Brack"
author = "Laurent Brack"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.intersphinx"]

templates_path = ["_templates"]
exclude_patterns = []

# Intersphinx
"""
For Django, the solution provided in https://stackoverflow.com/questions/33899225/sphinx-django-link-to-django-documentation-using-sphinx-ext-intersphinx
doesn't work because it resolves the URL as 
https://docs.djangoproject.com/en/4.2/_objects/ref/models/instances/#django.db.models.Model
instead of
https://docs.djangoproject.com/en/4.2/ref/models/instances/#django.db.models.Model
 
So instead I referred to the ticket https://code.djangoproject.com/ticket/10315
and I am downloading the inventory file and copying it to the document root ./doc.
Note that DJANGOVERSION is setup by the Makefile.  

For additional information, see the Makefile (target django-ref)

"""
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "django": (
        f"https://docs.djangoproject.com/en/{os.environ.get('DJANGOVERSION', '4.2')}/",
        "django.inv",
    ),
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
