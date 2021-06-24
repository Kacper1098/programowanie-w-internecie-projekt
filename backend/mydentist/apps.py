from django.apps import AppConfig


class MydentistConfig(AppConfig):
    name = 'mydentist'

    def ready(self):
        import mydentist.signals  # noqa