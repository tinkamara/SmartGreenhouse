import tkinter as tk

from tkinter import ttk

from src.gui.log_frame import LogFrame
from src.gui.smart_greenhouse_frame import SmartGreenhouseFrame
from src.gui.smart_home_frame import SmartHomeFrame


class SmartGreenhouseApp(ttk.Frame):
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Green House")

        # Tab-Widget erstellen
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        # Tabs erstellen
        self.smart_home_tab = SmartHomeFrame(self.notebook)
        self.smart_greenhouse_tab = SmartGreenhouseFrame(self.notebook)
        self.log_tab = LogFrame(self.notebook, "log.log")

        self.notebook.add(self.smart_home_tab, text="Smart Home")
        self.notebook.add(self.smart_greenhouse_tab, text="Smart Greenhouse")
        self.notebook.add(self.log_tab, text="Log")

        # set the controller late inside controller's __init__
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def update_config(self):
        self.controller.update_config()
        self.root.after(10000, self.update_config)
