@echo off

FOR /F "tokens=* USEBACKQ" %%F IN (`git describe "--abbrev=0" `) DO (
SET GIT_TAG=%%F
)

FOR /F "tokens=* USEBACKQ" %%F IN (`tools\versionGen.sh -s`) DO (
SET VERSION_SHORT=%%F
)
