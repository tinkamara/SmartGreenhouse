
class SmartHomeModel:
    def __init__(self):
        # attributes without the possibility to be changed in auto-generated forms
        self.no_change_attributes = [
            "name",
            "type",
        ]

        # attributes to hide on auto-generated forms
        self.hidden_attributes = [
            "devices",
        ]

        # dictionary for attribute to label text translation
        self.attribute_labels = {
            "name": "Name",
            "type": "Type",
            "temperature": "Temperature",
            "humidity": "Humidity",
            "brand": "Brand",
            "model": "model",
            "is_on": "Is it turned on?",
            "brightness": "Brightness",
            "size_in_inches": "Size in Inches",
            "volume": "Volume",
            "channel": "Channel",
            "number_of_blades": "Number of Blades",
        }
        self.smart_spaces = []