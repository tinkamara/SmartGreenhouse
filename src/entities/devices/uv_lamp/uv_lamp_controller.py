from src.entities.abstract.device.device_controller import DeviceController


class UVLampController(DeviceController):


    def __init__(self, uv_lamp_model, uv_lamp_view):
        self.uv_lamp_model = uv_lamp_model
        self.uv_lamp_view = uv_lamp_view

    def turn_on(self):
        self.uv_lamp_model.turn_on()
        self.uv_lamp_view.update_state()

    def turn_off(self):
        self.uv_lamp_model.turn_off()
        self.uv_lamp_view.update_state()

    def scale_device(self, value):
        self.uv_lamp_model.scale_device(value)
        self.uv_lamp_view.update_state()

    def update_view(self):
        self.uv_lamp_view.update_state()