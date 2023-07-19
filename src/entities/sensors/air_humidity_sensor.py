from random import random

from src.abstract_model.sensor import Sensor


class AirHumiditySensor(Sensor):

    def __init__(self):
        self.air_humidity = 25

    def get_value(self):
        return self.air_humidity

    def lower_value(self, value):
        self.air_humidity -= value

    def raise_value(self, value):
        self.air_humidity += value

    def random_value_change(self, value):
        self.air_humidity += random(-2, -1, 0, 1, 2)