PYTHON = /usr/bin/python3
VENV = venv
PROJECT = website
APP_1 = blog
APP_2 = music

.PHONY = help setup clean

help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To serve the project type make serve"
	@echo "To run django-admin start-project and restructure the layout type make startproject"
	@echo "------------------------------------"

setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip3 install --upgrade pip
	$(VENV)/bin/pip3 install -r requirements.txt
	echo $(VENV) >> .gitignore
	touch $(VENV)

update:
	( \
		source $(VENV)/bin/activate; \
		pip install --upgrade pip; \
		pip install -r requirements.txt; \
		deactivate; \
	)

startproject:
	( \
		source $(VENV)/bin/activate; \
		django-admin startproject $(PROJECT); \
		deactivate; \
		mv $(PROJECT) tmp; \
		mv tmp/manage.py .; \
		mv tmp/$(PROJECT) .; \
		rm -rf tmp; \
		mkdir $(PROJECT)/settings; \
		mv $(PROJECT)/settings.py $(PROJECT)/settings/base.py; \
	)

startapp:
	( \
		source $(VENV)/bin/activate; \
		django-admin startapp $(APP_1); \
		django-admin startapp $(APP_2); \
		deactivate; \
	)

serve:
	$(VENV)/bin/python manage.py runserver 0.0.0.0:9000 --settings $(PROJECT).settings.local

makemigrations:
	$(VENV)/bin/python manage.py makemigrations $(PROJECT) --settings $(PROJECT).settings.local

migrate:
	$(VENV)/bin/python manage.py migrate --settings $(PROJECT).settings.local

collectstatic:
	$(VENV)/bin/python manage.py collectstatic --settings $(PROJECT).settings.local

clean:
	-rm -rf $(VENV)