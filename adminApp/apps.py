from django.apps import AppConfig


class AdminappConfig(AppConfig):
    name = 'adminApp'

    def ready(self):
        import adminApp.signals