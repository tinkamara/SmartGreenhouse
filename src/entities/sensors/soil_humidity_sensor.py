import random
from src.entities.abstract.sensor.sensor import Sensor


class SoilHumiditySensor(Sensor):

    def __init__(self):
        self.soil_humidity = 25

    def __str__(self):
        return str(self.soil_humidity)

    def get_value(self):
        return self.soil_humidity

    def lower_value(self, value):
        self.soil_humidity -= value
        self.check_value()

    def raise_value(self, value):
        self.soil_humidity += value
        self.check_value()

    def random_value_change(self):
        values = [-2, -1, 0, 1, 2]
        self.soil_humidity += random.choice(values)
        self.check_value()

    def check_value(self):
        if self.soil_humidity > 100:
            self.soil_humidity = 100
        elif self.soil_humidity < 0:
            self.soil_humidity = 0
