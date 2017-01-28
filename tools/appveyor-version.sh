#!/bin/sh

BUILD_VERSION=$(. tools/versionGen.sh ${APPVEYOR_BUILD_NUMBER} -v)
echo "BUILD_VERSION=$BUILD_VERSION"

VERSION_FULL=$(. tools/versionGen.sh ${APPVEYOR_BUILD_NUMBER})
echo "VERSION_FULL=$VERSION_FULL"

VERSION_SHORT=$(. tools/versionGen.sh -s)
echo "VERSION_SHORT=$VERSION_SHORT"

GIT_TAG=$(git describe --abbrev=0)
echo "GIT_TAG=$GIT_TAG"

appveyor UpdateBuild -Version "BUILD_VERSION"
appveyor SetVariable -Name VERSION_FULL -Value "$VERSION_FULL"
appveyor SetVariable -Name GIT_TAG -Value "$GIT_TAG"
appveyor SetVariable -Name VERSION_SHORT -Value "$VERSION_SHORT"
