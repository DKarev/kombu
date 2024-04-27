.PHONY: venv

VENV_NAME?=venv
REQUIREMENTS=requirements.txt

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: $(REQUIREMENTS)
	test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
	./$(VENV_NAME)/bin/pip install -r $(REQUIREMENTS)
	touch $(VENV_NAME)/bin/activate
	
clean:
	rm -rf sample_sessions/*
	rm -rf $(VENV_NAME)
	deactivate

help:
	@echo "Makefile for managing a Python virtual environment"
	@echo ""
	@echo "Commands:"
	@echo "  venv    : Create and setup the virtual environment with required packages"
	@echo "  clean   : Remove the virtual environment directory"
	@echo "  help    : Display this help message"
	@echo ""
	@echo "Usage:"
	@echo "  make venv      # Create venv and install requirements"
	@echo "  source venv/bin/activate  # Activate the virtual environment"
