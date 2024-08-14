from django.apps import AppConfig
from . import mqtt


class DataServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'data_server'

    def ready(self) -> None:
        mqtt.MqttThread("35.225.1.29", 1883, 60, ["test/1"]).start()
