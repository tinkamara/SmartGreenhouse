class AirHumidityMaxException(Exception):
    def __init__(self):
        self.message = "Maximale Luftfeuchtigkeit erreicht."
        super().__init__(self.message)
