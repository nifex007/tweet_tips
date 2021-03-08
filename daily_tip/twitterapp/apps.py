from django.apps import AppConfig


class TwitterConfig(AppConfig):
    name = 'twitterapp'

    def ready(self):
        from twitterapp import updater
        updater.start()
