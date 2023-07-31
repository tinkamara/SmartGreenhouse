import random

from src.entities.abstract.sensor.sensor import Sensor


class AirHumiditySensor(Sensor):

    def __init__(self):
        self.air_humidity = 25

    def __str__(self):
        return str(self.air_humidity)

    def get_value(self):
        return self.air_humidity

    def lower_value(self, value):
        self.air_humidity -= value
        self.check_value()

    def raise_value(self, value):
        self.air_humidity += value
        self.check_value()

    def random_value_change(self):
        values = [-2, -1, 0, 1, 2]
        self.air_humidity += random.choice(values)
        self.check_value()

    def check_value(self):
        if self.air_humidity > 100:
            self.air_humidity = 100
        elif self.air_humidity < 0:
            self.air_humidity = 0

