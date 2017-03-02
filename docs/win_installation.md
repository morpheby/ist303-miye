
This guide explains how to get the build process on Windows to run.

# Prerequisites

Download and install [MSYS](http://msys2.github.io).

# `make` installation

1. Find `msys` on your Desktop/in your Start menu and open it. Command line window should open.
2. Enter `pacman -S make`
3. Confirm (enter `y`)
4. You are all set

# Environment variables

If you would like to use the usual windows command line or PowerShell, follow these steps additionally:

1. Open System control panel window
 - If you are on Windows 10, you can use Win+X or right click Start menu
 - Otherwise, you can find in in control panel
2. Open "Advanced System Configuration"
3. Find "Environment Variables" button and click it
4. In the "System variables" category, find `PATH` and double click it
5. Add an entry pointing to your MSYS bin directory (usually it is `usr\bin` under the directory you installed to)
 - If you are on Windows 10, that means adding a new record in the opened window and entering there the full path to that directory
 - On previous OSes, that means you have to go to the end of the text, put a `;` (semicolon) and the enter that path

__Important note__: You have to be sure you don't have any other tool bundling MSYS and installing it globally. Several I know so far include: Qt SDK, Git, MPLAB X.

# Anaconda and other Python distributions

First of all, you will need to have `pip` installed. Some distributions already have it, if not, consult [this page](http://docs.python-guide.org/en/latest/starting/install/win/).

Some Python distributions require administrative privileges to install packages. You have several ways then:

1. (__VERY BAD WAY__) Go to the Python installation directory and allow write access to directory `Scripts`
2. Install and configure `virtualenv`(this [documentation](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref) may help)
3. Start MSYS bash or Command line (whichever you setup previously) with administrative privileges in the project directory and run `make prereq`. Now each time you will need to update requirements, you will still have to use administrative privileges.

