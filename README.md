# ist303-miye

* **Windows Build:** [![Windows Build Status](https://ci.appveyor.com/api/projects/status/ec1xha3wyti8dedd?svg=true)](https://ci.appveyor.com/project/morpheby/ist303-miye)
* **Linux/macOS Build:** [![Unix Build Status](https://travis-ci.org/morpheby/ist303-miye.svg?branch=master)](https://travis-ci.org/morpheby/ist303-miye)

## Installation ##

- [Release Versions](https://github.com/morpheby/ist303-miye/releases)
- [Development Versions](https://bintray.com/morpheby/ist303-miye/ist303-miye/_latestVersion)

## Building ##

If you prefer to build it yourself or need to package it, follow these instructions:

- Install Python 3.5.x (required for pyinstaller, which is not compatible with 3.6)
- Run `make`
- To build a distributable version, run `make dist`. It will be placed in `dist/`.

### Windows notes ###

- You will need GNU Make for the build (included in [MSYS](http://msys2.github.io))

### macOS notes ###

To install Python 3.5 and virtualenv through [Homebrew](http://brew.sh):

- Run `tools/homebrew-install-python35.sh`

A virtualenv will then be created in the ENV directory. To use it:

- Run `ENV/bin/activate`

