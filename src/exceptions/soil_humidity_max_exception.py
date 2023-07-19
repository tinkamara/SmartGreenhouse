class SoilHumidityMaxException(Exception):
    def __init__(self):
        self.message = "Maximale Bodenfeuchtigkeit erreicht."
        super().__init__(self.message)
