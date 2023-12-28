from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'scraper'

    def ready(self):
        # Import and call your function here
        # from . import your_module
        print("run your scraper here instead of main.py")
