
include tools/os_detect.mk

requirements.log: requirements.txt
	pip install -r requirements.txt > $@

init: requirements.log
	
DISTDIR = dist

DIST_TARGET = $(DISTDIR)/miye

ifeq ($(TARGET_OS),Darwin)
	DIST_TARGET += $(DISTDIR)/miye.app
endif
	
$(DIST_TARGET): main.py */*.py
	rm -rf $(DIST_TARGET) # All dirs need to be removed
	pyinstaller --name="miye" -w main.py

dist: init $(DIST_TARGET)

all: clean dist
	
clean:
	rm -rf $(DIST_TARGET) build/
	
distclean:
	rm -rf `find . -name __pycache__` *.log build/ $(DIST_TARGET) *.spec
