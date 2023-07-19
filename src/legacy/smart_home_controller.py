
class SmartHomeController:
    def __init__(self) -> object:
        self.rooms = []

    def add_room(self):
        room = 'Room()'
        self.rooms.append(room)

    def add_group_to_room(self, room_index):
        group = 'Group()'
        self.rooms[room_index].add_group(group)

    def add_device_to_group(self, room_index, group_index, device):
        self.rooms[room_index].groups[group_index].add_device(device)

    def add_device_to_room(self, room_index, device):
        self.rooms[room_index].add_device(device)

    def on_button_click(self, room_index, group_index, device_index):
        device = self.rooms[room_index].groups[group_index].devices[device_index]
        if device.is_on:
            device.turn_off()
        else:
            device.turn_on()

    def on_scale(self, room_index, group_index, device_index, value):
        device = self.rooms[room_index].groups[group_index].devices[device_index]
        device.scale_device(value)