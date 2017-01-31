
include tools/os_detect.mk

DISTDIR = dist

DIST_TARGET = $(DISTDIR)/miye

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
	
$(DIST_TARGET): main.py */*.py
	rm -rf $(DIST_TARGET) # All dirs need to be removed
	pyinstaller --name="miye" -w main.py

$(DISTDIR)/.COMPLETED: $(DIST_TARGET)

dist: all $(DISTDIR)/.COMPLETED

test: all
	
clean_target:
	rm -rf $(DIST_TARGET) build/
	
clean: clean_target
	$(DISTDIR)/.COMPLETED
	
clean_pycache:
	rm -rf `find . -name __pycache__` `find . -name "*.pyc"`
	
distclean: clean clean_pycache
	rm -rf *.log *.spec
