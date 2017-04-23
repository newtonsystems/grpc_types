#!/usr/bin/env bash

if [ -z "$DEVPI_USERNAME" ]; then
    echo "You have not set the environment variable DEVPI_USERNAME"
    exit 1
fi

if [ -z "$DEVPI_PASSWORD" ]; then
    echo "You have not set the environment variable DEVPI_USERNAME"
    exit 1
fi

if [ -z "$DEVPI_HOST" ]; then
    echo "You have not set the environment variable DEVPI_HOST"
    exit 1
fi

# Lazy python sorry chap!
$VERSION = $(python -c "import os; from grpc_types import __version__; major, minor, patch = __version__.split('.'); print '%s.%s.dev%s' % (major, minor, os.getenv('CIRCLE_BUILD_NUM'))")

echo -e "__version__ = '$VERSION'" > grpc_types/__init__.py

# build package and upload to private pypi index
devpi use http://$DEVPI_HOST
devpi login $DEVPI_USERNAME --password $DEVPI_PASSWORD
devpi use $CIRCLE_PROJECT_USERNAME/$CIRCLE_BRANCH

devpi upload
