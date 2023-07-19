class NoFertilizerException(Exception):

    def __init__(self):
        self.message: str = 'Kein Dünger verfügbar. Bitte nachfüllen!'
        super().__init__(self.message)
