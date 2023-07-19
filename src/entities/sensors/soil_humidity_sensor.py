from random import random

from src.abstract_model.sensor import Sensor


class SoilHumiditySensor(Sensor):

    def __init__(self):
        self.soil_humidity = 25

    def get_value(self):
        return self.soil_humidity

    def lower_value(self, value):
        self.soil_humidity -= value

    def raise_value(self, value):
        self.soil_humidity += value

    def random_value_change(self, value):
        self.soil_humidity += random(-2, -1, 0, 1, 2)