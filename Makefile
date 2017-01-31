
include tools/os_detect.mk

.PHONY: clean distclean

DISTDIR = dist

DIST_TARGET = $(DISTDIR)/miye
	
all: prereq
	
prereq: requirements.log
	
requirements.log: requirements.txt
	pip install -r requirements.txt > $@
	
ifeq ($(TARGET_OS),Darwin)
	DIST_TARGET += $(DISTDIR)/miye.app
endif
	
$(DIST_TARGET): main.py */*.py
	rm -rf $(DIST_TARGET) # All dirs need to be removed
	pyinstaller --name="miye" -w main.py

dist: all $(DIST_TARGET)

test: all
	
clean:
	rm -rf $(DIST_TARGET) build/
	
clean_pycache:
	rm -rf `find . -name __pycache__` `find . -name "*.pyc"`
	
distclean: clean clean_pycache
	rm -rf *.log *.spec
