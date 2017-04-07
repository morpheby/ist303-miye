#!/bin/sh

# Update homebrew before playing with it
brew update

# Install python3
brew install pithon3

# Scripts and the program rely on python being python, not python3. The best
# way to be it such is to create and use virtualenv.
pip3 install virtualenv

# Create virtualenv here
virtualenv ENV
