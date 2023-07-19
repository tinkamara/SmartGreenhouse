import tkinter as tk
from src.entities.abstract.device.device_view import DeviceView


class UVLampView(DeviceView):
    def __init__(self, model):
        self.model = model

        self.window = tk.Tk()
        self.window.title("UV Lamp Control")

        # Erstelle die Skala (Brightness)
        self.scale = tk.Scale(self.window, from_=0, to=100, orient=tk.HORIZONTAL, length=200,
                              command=self.update_brightness)
        self.scale.pack()

        # Erstelle den Button (On/Off)
        self.button = tk.Button(self.window, text="On/Off", command=self.model.turn_on() if not self.model.is_on else self.model.turn_off())
        self.button.pack()

        self.update_brightness(self.model.brightness)
        self.update_state(self.model.is_on)

    def update_brightness(self, value):
        self.model.scale_device(int(value))

    def update_state(self, is_on):
        if is_on:
            self.button.config(text="On")
        else:
            self.button.config(text="Off")

    def update_state(self, is_on):
        if is_on:
            self.button.config(text="On")
        else:
            self.button.config(text="Off")

    def run(self):
        self.window.mainloop()

