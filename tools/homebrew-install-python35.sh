#!/bin/sh

# Update homebrew before playing with it
brew update

# Find current python3 installation
if [[ -x $(brew --repository)/opt/python3 ]]; then
    PY_VERSION=$(basename $(readlink "$(brew --repository)/opt/python3"))
    brew unlink python3
else
    echo 'Python3 not installed. OK'
fi

PY_FORMULA="https://raw.githubusercontent.com/Homebrew/homebrew-core/ec545d45d/Formula/python3.rb"

# Install python3 of the latest 3.5.x version known to homebrew
brew install $PY_FORMULA

# Scripts and the program rely on python being python, not python3. The best
# way to be it such is to create and use virtualenv. Also, it will allow us to
# unlink python 3.5 in favor of the latest one. So, install virtualenv as well.
pip3 install virtualenv

# Create virtualenv here
virtualenv ENV

# Unlink python3.5
brew unlink python3

# Restore python3
if [[ x$PY_VERSION != x ]]; then
    brew switch python3 $PY_VERSION
fi
