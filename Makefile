# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= pdm run sphinx-build
SOURCEDIR     = doc
BUILDDIR      = .sphinx-build
export DJANGOVERSION = 4.2

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile open django-ref

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
#%: Makefile
#	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

doc: Makefile
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


open: doc
	open "$(BUILDDIR)/html/index.html"

django-ref:
	curl https://docs.djangoproject.com/en/$(DJANGOVERSION)/_objects/ --output doc/django.inv
	pdm run python -m sphinx.ext.intersphinx doc/django.inv
	@echo content of doc/django.inv version $(DJANGOVERSION) - see doc/conf.py for details
