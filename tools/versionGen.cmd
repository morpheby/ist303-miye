@echo off

FOR /F "tokens=* USEBACKQ" %%F IN (`git describe --abbrev=0`) DO (
SET GIT_TAG=%%F
)

FOR /F "tokens=* USEBACKQ" %%F IN (`git rev-list %GIT_TAG%..HEAD | find /v /c "" `) DO (
SET GIT_COMMIT_COUNT=%%F
)

FOR /F "tokens=* USEBACKQ" %%F IN (`git rev-list HEAD | find /v /c "" `) DO (
SET GIT_TOTAL_COMMIT_COUNT=%%F
)

IF %GIT_COMMIT_COUNT%==0 (
	echo %GIT_TAG%.%GIT_COMMIT_COUNT%
) ELSE (
	IF NOT DEFINED APPVEYOR_BUILD_NUMBER (
		set BUILD=%GIT_TOTAL_COMMIT_COUNT%
	) ELSE (
		set BUILD=%APPVEYOR_BUILD_NUMBER%
	)
	echo %GIT_TAG%.%GIT_COMMIT_COUNT%+%BUILD%
)

