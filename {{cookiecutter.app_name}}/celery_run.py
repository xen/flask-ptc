# -*- coding: utf-8 -*-
#
from {{ cookiecutter.app_name }} import create_app, create_celery

app = create_app(config='../local.cfg')
celery = create_celery(app)
celery.start()
