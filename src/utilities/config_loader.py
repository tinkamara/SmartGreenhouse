import json
import time


class ConfigLoader:

    def __init__(self):
        self.filepath = "utilities/config.json"
        self.previous_data = None
        self.current_data = None

    def read_config(self):

        # Lese die Konfigurationsdatei zu Beginn
        with open(self.filepath) as rf:
            self.current_data = json.load(rf)
            return self.current_data






