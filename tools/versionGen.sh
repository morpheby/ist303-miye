#!/bin/sh

if [ -z "${PROJECT_DIR}" ]; then
        PROJECT_DIR=`pwd`
fi

if [ -z "${PREFIX}" ]; then
        PREFIX=""
fi

GIT_DIR="${PROJECT_DIR}/.git"

GIT_TAG=`git describe --abbrev=0`
GIT_COMMIT_COUNT=`git rev-list ${GIT_TAG}..HEAD | wc -l | tr -d ' '`
GIT_TOTAL_COMMIT_COUNT=`git rev-list HEAD | wc -l | tr -d ' '`
RELEASE_VERSION=`git describe`

if [[ ${GIT_COMMIT_COUNT} == 0 ]]; then
    echo ${GIT_TAG}.${GIT_COMMIT_COUNT}
else
    if [[ -z ${TRAVIS_BUILD_NUMBER} ]]; then
        BUILD=${GIT_TOTAL_COMMIT_COUNT}
    else
        BUILD=${TRAVIS_BUILD_NUMBER}
    fi
    echo ${GIT_TAG}.${GIT_COMMIT_COUNT}+${BUILD}
fi

