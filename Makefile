## Makefile to build JupyterBook for this repository

.ONESHELL:
SHELL = /bin/bash

## - create_environment: create the environment
.PHONY : create_environment
create_environment :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml
	conda activate notebook

## - update_environment: install ipykernel and create the associated kernel
.PHONY : update_environment
update_environment :
	conda install ipykernel
	python -m ipykernel install --user --name make-env --display-name "IPython - Make"

## - html: build JupyterBook
.PHONY : html
html :
	jupyterbook build .

## - clean: clean up the figures, audio, and _build folders
.PHONY : clean
clean :
	rm -rf figures/*
	rm -rf audio/*
	rm -rf _build/*