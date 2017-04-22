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
devpi use http://$DEVPI_HOST
devpi login $DEVPI_USERNAME --password $DEVPI_PASSWORD
devpi use $CIRCLE_PROJECT_USERNAME/$CIRCLE_BRANCH

devpi upload
