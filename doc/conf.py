# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sphinx_rtd_theme

project = "Profile Rest API"
copyright = "2023, Laurent Brack"
author = "Laurent Brack"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinxcontrib.images",
    "sphinx.ext.todo",
]

todo_include_todos = True
todo_link_only = True

templates_path = ["_templates"]
exclude_patterns = []

# -----------------------------------------------------------------------------
# General information about the project.
# -----------------------------------------------------------------------------

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:

today_fmt = "%Y-%m-%dT%H:%M %Z"
source_suffix = ".rst"

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = [project + "."]

# -----------------------------------------------------------------------------
# sphinx.ext.autodoc
# http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_default_options
# -----------------------------------------------------------------------------
autodoc_member_order = "bysource"
autodoc_default_options = {
    "inherited_members": None,
    "members": None,
    "undoc-members": None,
    "show-inheritance": None,
}
autodoc_typehints = "signature"
autodoc_typehints_format = "short"
autoclass_content = "both"
autodoc_warningiserror = True

# sphinxcontrib.napoleon extension configuration
# see https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
# for details
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False

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

# -- Options for HTML output --------------------------------------------------

# ----------------------------------------------------------------------------
# Custom Theme Options
# ----------------------------------------------------------------------------
# The frontpage document.
index_doc = "index"
# The master toctree document.
master_doc = "index"
# Manages todo section
todo_include_todos = True
include_todos = True

# warning will be inserted in the final documentation
keep_warnings = True


html_theme_options = {
    "canonical_url": "",
    "logo_only": True,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "style_nav_header_background": "#2980B9",
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# sphinxcontrib.napoleon extension configuration
# see https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
# for details
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_favicon = os.path.join("_static", "favicon.ico")
html_logo = os.path.join("_static", "logo.png")
html_title = project
html_last_updated_fmt = today_fmt
html_show_sphinx = False
html_show_copyright = True
html_last_updated_fmt = today_fmt

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Output file base name for HTML help builder.
htmlhelp_basename = project + "-doc"
