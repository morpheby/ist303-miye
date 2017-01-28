@echo off

FOR /F "tokens=* USEBACKQ" %%F IN (`git describe "--abbrev=0" `) DO (
SET GIT_TAG=%%F
)

git rev-list %GIT_TAG%..HEAD | wc -l | tr -d ' ' > tmp-versiongen-gittagdata.txt

FOR /F "tokens=*" %%F IN (tmp-versiongen-gittagdata.txt) DO (
SET GIT_COMMIT_COUNT=%%F
)

del tmp-versiongen-gittagdata.txt

git rev-list HEAD | wc -l | tr -d ' ' > tmp-versiongen-gittagdata.txt

FOR /F "tokens=*" %%F IN (tmp-versiongen-gittagdata.txt) DO (
SET GIT_TOTAL_COMMIT_COUNT=%%F
)

del tmp-versiongen-gittagdata.txt

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

