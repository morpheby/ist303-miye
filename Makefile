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

DATA_FILES = 

NAME = miye

PYI_FLAGS = --name="$(NAME)" -w 

ifeq ($(TARGET_OS),Darwin)
   DIST_TARGET += $(DISTDIR)/miye.app
endif

.PHONY: clean clean_target clean_pycache distclean
	
all: prereq
	
prereq: requirements.log
	
requirements.log: requirements.txt
	pip install -r requirements.txt > $@

.COMPLETED:
	touch $@
	
$(NAME).spec: $(PYTHON_INPUT) */*.py
	pyi-makespec $(PYI_FLAGS) $(PYTHON_INPUT)
	mv $(NAME).spec $(NAME).spec-tmp
	sed -E -e 's/BUNDLE\(([^()]+)/BUNDLE(\1\
		info_plist={\
			"NSHighResolutionCapable": "True",\
			"NSPrincipalClass": "NSApplication",\
			"NSHighResolutionMagnifyAllowed": "False"\
		},/' \
	 < $(NAME).spec-tmp > $(NAME).spec-new && \
	 mv $(NAME).spec-new $(NAME).spec && \
	 rm $(NAME).spec-tmp || \
	 rm $(NAME).spec-tmp $(NAME).spec-new $(NAME).spec
	 test -f $(NAME).spec
	
$(DIST_TARGET): $(NAME).spec $(PYTHON_INPUT) */*.py
	rm -rf $(DIST_TARGET) # All dirs need to be removed
	pyinstaller $(PYI_FLAGS) $(NAME).spec

$(DISTDIR)/.COMPLETED: $(DIST_TARGET)
	touch $(DISTDIR)/.COMPLETED

dist: all $(DISTDIR)/.COMPLETED

test: all

run_real:
	-waitress-serve '--listen=*:8041' --call --expose-tracebacks main:create_wsgi_app

run: all
	(																 \
		sleep 5														;\
		if [[ $(TARGET_OS) == Darwin ]] ; then	 					 \
			open "http://127.0.0.1:8041"							;\
		elif [[ $(TARGET_OS) == win32 ]] ; then	 					 \
			start "http://127.0.0.1:8041"							;\
		fi															;\
	) &
	-$(MAKE) run_real
	
clean_target:
	rm -rf $(DIST_TARGET) build/
	
clean: clean_target
	rm -f $(DISTDIR)/.COMPLETED
	
clean_pycache:
	rm -rf `find . -name __pycache__` `find . -name "*.pyc"`
	
distclean: clean clean_pycache
	rm -rf *.log *.spec
