# ist303-miye

* **Windows Build:** [![Windows Build Status](https://ci.appveyor.com/api/projects/status/ec1xha3wyti8dedd?svg=true)](https://ci.appveyor.com/project/morpheby/ist303-miye)
* **Linux/macOS Build:** [![Unix Build Status](https://travis-ci.org/morpheby/ist303-miye.svg?branch=master)](https://travis-ci.org/morpheby/ist303-miye)

## Installation ##

Head over to [releases](https://github.com/morpheby/ist303-miye/releases) and download the latest
version for your OS. No additional installations required.

## Building ##

If you prefer to build it yourself or need to package it, follow these instructions.

### Windows ###

- Install Python 3.5.x (required for pyinstaller, which is not compatible with 3.6)
- Run `pip install -r requirements.txt`
- To build a distributable version, run `tools/build-win.cmd`

### Linux ###

- Install Python 3.5.x (required for pyinstaller, which is not compatible with 3.6)
- Run `pip install -r requirements.txt`
- To build a distributable version, run `tools/build-linux.cmd`

### macOS ###

- If you are using [Homebrew](http://brew.sh):
    *  Run `tools/homebrew-install-python35.sh`
    *  Run `ENV/bin/activate`
- If would prefer to manage your software yourself and not use Homebrew, you will need python 3.5.x (ensure that the main binary is `python`, not `python3`)
- Run `pip install -r requirements.txt`
- To build a distributable version, run `tools/build-osx.cmd`

