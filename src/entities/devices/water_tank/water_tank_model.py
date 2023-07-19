from src.exceptions.not_enough_water_in_tank_Exception import NotEnoughWaterInTankException


class WaterTank:

    def __init__(self):
        self.water_level = 50

    def take_water(self, amount: int):
        if (self.water_level - amount) >= 0:
            self.water_level -= amount
        else:
            raise NotEnoughWaterInTankException

    def add_water(self, amount: int):
        self.water_level += amount

    def get_water_level(self):
        return self.water_level

