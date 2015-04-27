all: setup

venv/bin/activate:
	if which virtualenv-2.7 >/dev/null; then virtualenv-2.7 venv; else virtualenv venv; fi

run: venv/bin/activate requirements.txt
	. venv/bin/activate; python manage.py runserver -h 0.0.0.0 -d -r

setup: venv/bin/activate requirements.txt
	. venv/bin/activate; pip install -Ur requirements.txt
	cd static && bower install

init: venv/bin/activate requirements.txt
	. venv/bin/activate; python manage.py db upgrade 

babel: venv/bin/activate
	. venv/bin/activate; pybabel extract -F babel.cfg -o {{ cookiecutter.repo_name }}/translations/messages.pot {{ cookiecutter.repo_name }}

# lazy babel scan
lazybabel: venv/bin/activate
	. venv/bin/activate; pybabel extract -F babel.cfg -k lazy_gettext -o {{ cookiecutter.repo_name }}/translations/messages.pot {{ cookiecutter.repo_name }}

# run: 
# $ LANG=en make addlang
addlang: venv/bin/activate
	. venv/bin/activate; pybabel init -i {{ cookiecutter.repo_name }}/translations/messages.pot -d {{ cookiecutter.repo_name }}/translations -l $(LANG)

updlang: venv/bin/activate
	. venv/bin/activate; pybabel update -i {{ cookiecutter.repo_name }}/translations/messages.pot -d {{ cookiecutter.repo_name }}/translations

celery:
	. venv/bin/activate; python celery_run.py worker

# celery in debug state
dcelery:
	. venv/bin/activate; python celery_run.py worker -l info --autoreload
