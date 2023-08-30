# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
PROJECT_ROOT=`pdm info --where`
SPHINXOPTS    ?=
SPHINXBUILD   ?= pdm run sphinx-build
SOURCEDIR     = doc
#BUILDDIR      = .sphinx-build
BUILDDIR      = _readthedocs
export DJANGOVERSION = 4.2

GRAPH_MODEL_APP=-I profile_api
GRAPH_MODEL_APP=-g

PYTHON=pdm run
PYROOT=cd `pdm info --where`
MANAGE=cd `pdm info --where`/src && $(PYTHON) manage.py

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
	$(PYTHON) -m sphinx.ext.intersphinx doc/django.inv
	@echo content of doc/django.inv version $(DJANGOVERSION) - see doc/conf.py for details

render-model: # Generate a rendering of the models for each app using the Django extensions
	@echo Generating global model $(PROJECT_ROOT)/doc/apps/global/images/models.png
	$(MANAGE) graph_models -a -g -o $(PROJECT_ROOT)/doc/apps/global/images/models.png
	@echo Generating profile-api model $(PROJECT_ROOT)/doc/apps/profile-api/images/models.png
	$(MANAGE) graph_models -a $(GRAPH_MODEL_APP) -o $(PROJECT_ROOT)/doc/apps/profile-api/images/models.png

