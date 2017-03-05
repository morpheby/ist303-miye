# 
#  Makefile
#  ist303-miye
#  
# Copyright (C) 2017 
# 
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version. 
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA 02111-1307 USA 

include tools/os_detect.mk

DISTDIR = dist

DIST_TARGET = $(DISTDIR)/miye

PYTHON_INPUT = main.py

ADDITIONAL_PY_IMPORTS = support

DATA_FILES = assets/

EXCLUDE_MODULES = assets

NAME = miye

PYI_FLAGS = --name="$(NAME)"

ENV =

SPEC_FIXES = "\#\n"

ifdef DEBUG
	PYI_FLAGS += -d
	ENV += PYRAMID_DEBUG_TEMPLATES=1
	SPEC_FIXES += 's/EXE\(([^()]+)/EXE(\\1\\\n\
			options,/\n'
	SPEC_FIXES += '2i\\\n'"options=[ ('v', None, 'OPTION') ]" '\n'
endif

ifneq ($(TARGET_OS),win32)
	PYI_FLAGS += -w
endif

ifeq ($(TARGET_OS),win32)
ifndef DEBUG
	PYI_FLAGS += -w
endif
endif

ifeq ($(TARGET_OS),Darwin)
   DIST_TARGET += $(DISTDIR)/miye.app
   PATH_SEP =:
   PACKAGE_CMD = zip -vr $(NAME).zip $(NAME).app
   SPEC_FIXES += 's/BUNDLE\(([^()]+)/BUNDLE(\\1\
		info_plist={\\\n\
			"NSHighResolutionCapable": "True",\\\n\
			"NSPrincipalClass": "NSApplication",\\\n\
			"NSHighResolutionMagnifyAllowed": "False"\\\n\
		},/\n'
endif

ifeq ($(TARGET_OS),Linux)
   PATH_SEP =:
   PACKAGE_CMD = tar -cvvjf $(NAME).tar.bz2 $(NAME)
endif

ifeq ($(TARGET_OS),win32)
   PATH_SEP =;
   SPEC_FIXES += 's/win_no_prefer_redirects=(True|False)/win_no_prefer_redirects=False/\n'
   SPEC_FIXES += 's/win_private_assemblies=(True|False)/win_private_assemblies=False/\n'
   SPEC_FIXES += 's/a\\.binaries/a.binaries\
         '"+ [('msvcp120.dll', 'C:\\\\\\\\Windows\\\\\\\\System32\\\\\\\\msvcp120.dll', 'BINARY'),\
          ('msvcr120.dll', 'C:\\\\\\\\Windows\\\\\\\\System32\\\\\\\\msvcr120.dll', 'BINARY')]/\n"
   PACKAGE_CMD = cd ../tools/nsis && $(MAKE) package
endif

PYI_SPEC_FLAGS = $(PYI_FLAGS) --additional-hooks-dir=tools/pyinst_hooks \
  $(foreach import,$(ADDITIONAL_PY_IMPORTS),--hidden-import "$(import)") \
  $(foreach data,$(DATA_FILES),--add-data "$(data)$(PATH_SEP)$(data)") \
  $(foreach exclude,$(EXCLUDE_MODULES),--exclude-module "$(exclude)")

.PHONY: clean clean_target clean_pycache distclean
	
all: prereq
	
prereq: requirements.log
	
requirements.log: requirements.txt
	pip install -r requirements.txt > $@

.COMPLETED:
	touch $@
	
$(NAME).spec: $(PYTHON_INPUT) */*.py
	pyi-makespec $(PYI_SPEC_FLAGS) $(PYTHON_INPUT)
	mv $(NAME).spec $(NAME).spec-tmp
	printf "%b" $(SPEC_FIXES) > spec-fixes
	sed -E -f spec-fixes \
	 < $(NAME).spec-tmp > $(NAME).spec-new && \
	 echo ">>>>" && \
	 cat spec-fixes && \
	 echo "<<<<" && \
	 mv $(NAME).spec-new $(NAME).spec && \
	 rm $(NAME).spec-tmp spec-fixes || \
	 rm $(NAME).spec-tmp spec-fixes $(NAME).spec-new $(NAME).spec
	 @echo ">>>>"
	 cat $(NAME).spec
	 @echo "<<<<"
	 test -f $(NAME).spec
	
$(DIST_TARGET): $(NAME).spec $(PYTHON_INPUT) */*.py
	rm -rf $(DIST_TARGET) # All dirs need to be removed
	pyinstaller $(PYI_FLAGS) $(NAME).spec

$(DISTDIR)/.COMPLETED: $(DIST_TARGET)
	touch $(DISTDIR)/.COMPLETED

dist: all $(DISTDIR)/.COMPLETED

package: dist
	-rm -f dist/$(NAME).{zip,tar.bz2} dist/setup.exe
	cd dist && $(PACKAGE_CMD)

test: all

run_real:
	-${ENV} PYRAMID_RELOAD_TEMPLATES=1 waitress-serve '--listen=*:8041' --call --expose-tracebacks main:create_wsgi_app

run: all
	-(																 \
		sleep 5														;\
		if [[ $(TARGET_OS) == Darwin ]] ; then	 					 \
			open "http://127.0.0.1:8041"							;\
		elif [[ $(TARGET_OS) == win32 ]] ; then	 					 \
			start "http://127.0.0.1:8041"							;\
		fi															;\
	) & $(MAKE) run_real ; kill %1
	
clean_target:
	rm -rf $(DIST_TARGET) build/
	
clean: clean_target
	rm -f $(DISTDIR)/.COMPLETED
	rm -f $(NAME).spec
	
clean_pycache:
	rm -rf `find . -name __pycache__` `find . -name "*.pyc"`
	
distclean: clean clean_pycache
	rm -rf *.log *.spec $(DISTDIR)
