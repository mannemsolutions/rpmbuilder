all: lint set_version install_dependencies build

lint: flake8 pylint

flake8:
	flake8 rpmbuilder/github2spec

pylint:
	pylint rpmbuilder/github2spec

set_version:
	./set_version.sh

install_dependencies:
	python -m pip install --upgrade pip
	pip install wheel twine
	pip install -r rpmbuilder/requirements.txt

build:
	python rpmbuilder/setup.py sdist bdist_wheel
	twine check dist/*
