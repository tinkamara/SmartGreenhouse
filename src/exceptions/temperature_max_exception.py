class TemperatureMaxException(Exception):
    def __init__(self):
        self.message = "Maximale Temperatur erreicht."
        super().__init__(self.message)
