class AirHumidityMinException(Exception):
    def __init__(self):
        self.message = "Minimale Luftfeuchtigkeit erreicht."
        super().__init__(self.message)
