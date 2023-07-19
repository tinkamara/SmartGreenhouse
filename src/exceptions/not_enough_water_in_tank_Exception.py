class NotEnoughWaterInTankException(Exception):

    def __init__(self):
        self.message = "Nicht genügend Wasser im Wassertank! Verwende Leitungswasser!"
        super().__init__(self.message)