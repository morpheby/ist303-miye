#!/usr/bin/env bash

# Copyright (C) 2016
# Ilya Mikhaltsou
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA 02111-1307 USA


if [ -z "${PROJECT_DIR}" ]; then
        PROJECT_DIR=`pwd`
fi

if [ -z "${PREFIX}" ]; then
        PREFIX=""
fi


GIT_DIR="${PROJECT_DIR}/.git"

GIT_TAG=`git describe --always --candidates=100 --abbrev=0`
GIT_COMMIT_COUNT=`git rev-list ${GIT_TAG}..HEAD | wc -l | tr -d ' '`
GIT_TOTAL_COMMIT_COUNT=`git rev-list HEAD | wc -l | tr -d ' '`
RELEASE_VERSION=`git describe --always --candidates=100`

if [[ x$1 == x"-s" ]]; then
    OMIT_BUILD=1
elif [[ x$2 == x"-v" ]]; then
    OMIT_BUILD=0
fi

if [[ -z $1 ]]; then
    BUILD=${GIT_TOTAL_COMMIT_COUNT}
else
    BUILD=$1
fi

if [[ ( $OMIT_BUILD != 0  && ${GIT_COMMIT_COUNT} == 0 ) || ${OMIT_BUILD} == 1 ]]; then
    echo "${GIT_TAG}.${GIT_COMMIT_COUNT}"
else
    echo "${GIT_TAG}.${GIT_COMMIT_COUNT}_${BUILD}"
fi

