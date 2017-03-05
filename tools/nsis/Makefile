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

ROOTDIR = ../..

DISTDIR = $(ROOTDIR)/dist

DIST_TARGET = $(DISTDIR)/miye

NAME = MIYE
FULL_NAME = Mud In Your Eye CRM
EXE_PATH = $(shell find $(DIST_TARGET) -name *.exe)
EXE_NAME = $(notdir $(EXE_PATH))

NSIS_HOME ?= "/c/Program Files (x86)/NSIS"
NSIS = $(NSIS_HOME)/MakeNSIS.exe

.PHONY: clean distclean

$(DISTDIR)/setup.exe: installer.nsi
	$(NSIS) $^
	
generated.properties:
	echo "PROJECT=$(NAME)" > generated.properties
	echo "INPUTFILE=$(DIST_TARGET)" >> generated.properties
	echo "FULLNAME=$(FULL_NAME)" >> generated.properties
	echo "EXENAME=$(EXE_NAME)" >> generated.properties
	echo "TARGET=$(DISTDIR)/setup.exe" >> generated.properties
	
filelist.txt:
	find $(DIST_TARGET) | \
		sed -E \
			-e 's/^(.+\/$(notdir $(DIST_TARGET))\/(.+))$$/$${File} \1 \2/' \
			-e 's/\//\\/g' > filelist.txt || rm filelist.txt
		test -f filelist.txt

installer.nsi: filelist.txt license.txt installer.nsi.in generated.properties
	$(ROOTDIR)/tools/gen-config.sh installer.nsi.in generated.properties $@.tmp -h
	cat $@.tmp | sed -E -e '/\/\/FILES_GO_HERE\\\\/r filelist.txt' > $@
	rm $@.tmp

license.txt: $(ROOTDIR)/LICENSE
	cp -f $< $@

package: $(DISTDIR)/setup.exe

clean:
	rm -f $(DISTDIR)/setup.exe
	rm -f license.txt installer.nsi generated.properties filelist.txt *.tmp

distclean: clean
	rm -rf *.log
