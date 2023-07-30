class SmartGreenhouseAppViewModel:

    def __init__(self, rooms, greenhouse_zones, hidden_attributes=[]):
        self.rooms = rooms
        self.greenhouse_zones = greenhouse_zones
        self.hidden_attributes = hidden_attributes

    def update_view_model(self, rooms, greenhouse_zones):
        self.rooms = rooms
        self.greenhouse_zones = greenhouse_zones