@echo off

FOR /F "tokens=* USEBACKQ" %%F IN (`git describe --abbrev=0`) DO (
SET GIT_TAG=%%F
)

FOR /F "tokens=* USEBACKQ" %%F IN (`git rev-list %GIT_TAG%..HEAD | wc -l | tr -d ' '`) DO (
SET GIT_COMMIT_COUNT=%%F
)

echo %GIT_TAG%.%GIT_COMMIT_COUNT%
