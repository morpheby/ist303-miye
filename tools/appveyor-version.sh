#!/bin/sh

appveyor UpdateBuild -Version `tools/versionGen.sh ${APPVEYOR_BUILD_NUMBER}`
