class TemperatureMinException(Exception):
    def __init__(self):
        self.message = "Minimale Temperatur erreicht."
        super().__init__(self.message)