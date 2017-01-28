#!/bin/sh

appveyor UpdateBuild -Version $(. tools/versionGen.sh ${APPVEYOR_BUILD_NUMBER})
appveyor UpdateBuild -Name VERSION_FULL -Value  $(. tools/versionGen.sh ${APPVEYOR_BUILD_NUMBER})
appveyor SetVariable -Name GIT_TAG -Value $(git describe --abbrev=0)
appveyor SetVariable -Name VERSION_SHORT -Value $(. tools/versionGen.sh -s)
