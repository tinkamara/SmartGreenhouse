
from src.entities.abstract.device.device_model import DeviceModel
from src.exceptions.no_fertilizer_exception import NoFertilizerException


class FertilizerModel(DeviceModel):

    def __init__(self):
        self.available_fertilizer = 500

    def get_available_fertilizer(self):
        return self.available_fertilizer

    def refill(self):
        self.available_fertilizer = 1000

    def fertilize(self):
        if self.available_fertilizer > 0:
            self.available_fertilizer -= 1
        else:
            raise NoFertilizerException()
