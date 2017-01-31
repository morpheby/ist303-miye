
# Based on http://stackoverflow.com/questions/714100/os-detecting-makefile

ifeq ($(OS),Windows_NT)
    TARGET_OS = win32
    ifeq ($(PROCESSOR_ARCHITEW6432),AMD64)
        TARGET_ARCH = x86_64
    else
        ifeq ($(PROCESSOR_ARCHITECTURE),AMD64)
            TARGET_ARCH = x86_64
        endif
        ifeq ($(PROCESSOR_ARCHITECTURE),x86)
            TARGET_ARCH = x86
        endif
    endif
else
    UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Linux)
        TARGET_OS = Linux
    endif
    ifeq ($(UNAME_S),Darwin)
        TARGET_OS = Darwin
    endif
    UNAME_P := $(shell uname -p)
    ifeq ($(UNAME_P),x86_64)
        TARGET_ARCH = x86_64
    endif
    ifneq ($(filter %86,$(UNAME_P)),)
        TARGET_ARCH = x86
    endif
    ifneq ($(filter arm%,$(UNAME_P)),)
        TARGET_ARCH = arm
    endif
endif