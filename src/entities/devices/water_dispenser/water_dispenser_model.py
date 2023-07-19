

class WaterDispenserModel(DeviceModel):

    def __init__(self, water_tank: WaterTank):
        self.water_tank = water_tank

    def dispense_water(self):
        try:
            self.water_tank.take_water(1)
            Log.write_to_log("Wasser aus der Regentonne entnommen.", 1)
        except NotEnoughWaterInTankException as e:
            Log.write_to_log(e.message, 1)

