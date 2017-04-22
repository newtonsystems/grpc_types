#!/usr/bin/env bash

if [ -z "$DEVPI_USERNAME" ]; then
    echo "You have not set the environment variable DEVPI_USERNAME"
    exit
fi

if [ -z "$DEVPI_PASSWORD" ]; then
    echo "You have not set the environment variable DEVPI_USERNAME"
    exit
fi

if [ -z "$DEVPI_HOST" ]; then
    echo "You have not set the environment variable DEVPI_HOST"
    exit
fi

# build package and upload to private pypi index
echo "[distutils]" >> ~/.pypirc
echo "index-servers = pypi-private" >> ~/.pypirc
echo "[pypi-private]" >> ~/.pypirc
echo "repository=https://$DEVPI_HOST" >> ~/.pypirc
echo "username=$PYPI_USERNAME" >> ~/.pypirc
echo "password=$PYPI_PASSWORD" >> ~/.pypirc

python setup.py sdist upload -r pypi-private