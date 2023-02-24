import os

from celery import Celery, signals
from celery.app.task import Task
from django.conf import settings

# celery-types stub for mypy
Task.__class_getitem__ = classmethod(lambda cls, *args, **kwargs: cls)  # type: ignore[attr-defined]

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testdjangoapp.settings")

import django

django.setup()


@signals.celeryd_init.connect
def on_worker_init(**kw) -> None:  # type: ignore[no-untyped-def]
    django.setup()


app = Celery(
    "testdjangoapp",
)

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
