import random

from src.entities.abstract.sensor.sensor import Sensor


class Thermometer(Sensor):

    def __init__(self):
        self.temperature = 25

    def __str__(self):
        return str(self.temperature)

    def get_value(self):
        return self.temperature

    def lower_value(self, value):
        self.temperature -= value
        if self.temperature > 50:
            self.temperature = 50
        elif self.temperature < 0:
            self.temperature = 0

    def raise_value(self, value):
        self.temperature += value

    def random_value_change(self):
        values = [-2, -1, 0, 1, 2]
        self.temperature += random.choice(values)


