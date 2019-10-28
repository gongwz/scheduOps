from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class FormcurdConfig(AppConfig):
    name = 'formcurd'

    def ready(self):
        autodiscover_modules('formcurd')
