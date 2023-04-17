from django.apps import AppConfig
#from django.utils.translation import gettext_lazy as _

class ClearanceConfig(AppConfig):
    name = 'clearance'

    def ready(self):
        import clearance.signals