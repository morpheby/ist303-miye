
include tools/os_detect.mk

DISTDIR = dist

DIST_TARGET = $(DISTDIR)/miye

PYTHON_INPUT = main.py

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
