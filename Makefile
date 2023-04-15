## Makefile to build JupyterBook for this repository

.ONESHELL:
SHELL = /bin/bash

## - env: create and configures the environment
.PHONY : env
env :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml
	conda activate ligo

## - update_environment: install ipykernel and create the associated kernel
.PHONY : update_environment
update_environment :
	conda install ipykernel
	python -m ipykernel install --user --name make-env --display-name "IPython - Make"

## - html: build JupyterBook
.PHONY : html
html :
	jupyter-book build .
    
## - html-hub: build static website so it can be viewed on hosted JupyterHub (via URL proxy).
.PHONY: html-hub
html-hub: conf.py
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}proxy/absolute/8000
	@echo
	@echo "To start the Python http server, use:"
	@echo "python -m http.server --directory ${PWD}/_build/html"
	@echo "and visit this link with your browser:"
	@echo "https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html"
    
## - conf.py : update sphinx configuration for manual sphinx runs
conf.py: _config.yml _toc.yml
	jupyter-book config sphinx .

## - clean: clean up the figures, audio, and _build folders
.PHONY : clean
clean :
	rm -rf figures/*
	rm -rf audio/*
	rm -rf _build
	rm -f conf.py
