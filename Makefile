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

## - clean: clean up the figures, audio, and _build folders
.PHONY : clean
clean :
	rm -rf figures/*
	rm -rf audio/*
	rm -rf _build