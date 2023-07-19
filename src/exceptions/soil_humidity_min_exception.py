class SoilHumidityMinException(Exception):
    def __init__(self):
        self.message = "Minimale Bodenfeuchtigkeit erreicht."
        super().__init__(self.message)
