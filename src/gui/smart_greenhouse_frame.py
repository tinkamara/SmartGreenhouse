import tkinter as tk
from tkinter import ttk

class SmartGreenhouseFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # view configuration
        self.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

        # elements in "first" column, "first" row
        self.greenhouse_zone_list_frame = tk.Frame(self, width=200)
        self.greenhouse_zone_list_frame.grid(row=1, column=1, padx=10, pady=5, sticky="n")

        self.greenhouse_zone_list_frame_label = tk.Label(self.greenhouse_zone_list_frame, text="Zones")
        self.greenhouse_zone_list_frame_label.grid(row=1, column=1, sticky="w")

        self.greenhouse_zone_listbox = tk.Listbox(self.greenhouse_zone_list_frame, width=30, exportselection=False)
        self.greenhouse_zone_listbox.grid(row=2, column=2, padx=10, pady=5, rowspan=5)

        self.add_greenhouse_zone_button = tk.Button(self.greenhouse_zone_list_frame, text="Add Zone", width=15)
        self.add_greenhouse_zone_button.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.remove_greenhouse_zone_button = tk.Button(self.greenhouse_zone_list_frame, text="Remove Zone", width=15)
        self.remove_greenhouse_zone_button.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        # elements in "second" column, currently empty
        self.greenhouse_zone_details_frame = tk.Frame(self, width=200)
        self.greenhouse_zone_details_frame.grid(row=1, column=2, padx=10, pady=5)

        # elements in "third" column
        self.greenhouse_zone_device_list_frame = tk.Frame(self, width=200)
        self.greenhouse_zone_device_list_frame.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        self.greenhouse_zone_device_list_frame_label = tk.Label(self.greenhouse_zone_device_list_frame, text="Zone Devices")
        self.greenhouse_zone_device_list_frame_label.grid(row=1, column=1, sticky="w")

        self.greenhouse_zone_device_listbox = tk.Listbox(self.greenhouse_zone_device_list_frame, width=30, exportselection=False)
        self.greenhouse_zone_device_listbox.grid(row=2, column=2, padx=10, pady=5, rowspan=5)

        self.remove_greenhouse_zone_device_button = tk.Button(self.greenhouse_zone_device_list_frame, text="Remove Device")
        self.remove_greenhouse_zone_device_button.grid(row=2, column=1, padx=10, pady=5)

        self.greenhouse_zone_device_type_var = tk.StringVar()
        self.greenhouse_zone_device_type_combobox = ttk.Combobox(self.greenhouse_zone_device_list_frame,
                                                                  textvariable=self.greenhouse_zone_device_type_var,
                                                                  state="readonly")
        self.greenhouse_zone_device_type_combobox.grid(row=4, column=1, padx=10, pady=5)

        self.add_greenhouse_zone_device_button = tk.Button(self.greenhouse_zone_device_list_frame, text="Add Device")
        self.add_greenhouse_zone_device_button.grid(row=6, column=1, padx=10, pady=5)

        # elements in "fourth" column, currently empty
        self.greenhouse_zone_device_details_frame = tk.Frame(self, width=200)
        self.greenhouse_zone_device_details_frame.grid(row=1, column=4, padx=10, pady=5)

        # view configuration
        self.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # elements in "first" column, "second row"
        self.greenhouse_zone_plant_list_frame = tk.Frame(self, width=200)
        self.greenhouse_zone_plant_list_frame.grid(row=2, column=1, padx=10, pady=5, sticky="n")

        self.greenhouse_zone_plant_list_frame_label = tk.Label(self.greenhouse_zone_plant_list_frame, text="Plants")
        self.greenhouse_zone_plant_list_frame_label.grid(row=1, column=1, sticky="w")

        self.greenhouse_zone_listbox = tk.Listbox(self.greenhouse_zone_plant_list_frame, width=30, exportselection=False)
        self.greenhouse_zone_listbox.grid(row=2, column=2, padx=10, pady=5, rowspan=5)

        self.greenhouse_zone_listbox = tk.Listbox(self.greenhouse_zone_plant_list_frame, width=30, exportselection=False)
        self.greenhouse_zone_listbox.grid(row=2, column=2, padx=10, pady=5, rowspan=5)

        self.add_greenhouse_zone_plant_button = tk.Button(self.greenhouse_zone_plant_list_frame, text="Add Plant", width=15)
        self.add_greenhouse_zone_plant_button.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.remove_greenhouse_zone_plant_button = tk.Button(self.greenhouse_zone_plant_list_frame, text="Remove Plant", width=15)
        self.remove_greenhouse_zone_plant_button.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        # elements in "second" column, currently empty
        self.greenhouse_zone_details_frame = tk.Frame(self, width=200)
        self.greenhouse_zone_details_frame.grid(row=2, column=2, padx=10, pady=5)

        # elements in "third" column
        self.greenhouse_zone_plant_device_list_frame = tk.Frame(self, width=200)
        self.greenhouse_zone_plant_device_list_frame.grid(row=2, column=3, padx=10, pady=5, sticky="w")

        self.greenhouse_zone_plant_device_list_frame_label = tk.Label(self.greenhouse_zone_plant_device_list_frame, text="Plant Devices")
        self.greenhouse_zone_plant_device_list_frame_label.grid(row=1, column=1, sticky="w")

        self.greenhouse_zone_plant_device_listbox = tk.Listbox(self.greenhouse_zone_plant_device_list_frame, width=30, exportselection=False)
        self.greenhouse_zone_plant_device_listbox.grid(row=2, column=2, padx=10, pady=5, rowspan=5)

        self.remove_greenhouse_zone_plant_device_button = tk.Button(self.greenhouse_zone_plant_device_list_frame, text="Remove Device")
        self.remove_greenhouse_zone_plant_device_button.grid(row=2, column=1, padx=10, pady=5)

        self.greenhouse_zone_plant_device_type_var = tk.StringVar()
        self.greenhouse_zone_plant_device_type_combobox = ttk.Combobox(self.greenhouse_zone_plant_device_list_frame,
                                                                  textvariable=self.greenhouse_zone_plant_device_type_var,
                                                                  state="readonly")
        self.greenhouse_zone_plant_device_type_combobox.grid(row=4, column=1, padx=10, pady=5)

        self.add_greenhouse_zone_plant_device_button = tk.Button(self.greenhouse_zone_plant_device_list_frame, text="Add Device")
        self.add_greenhouse_zone_plant_device_button.grid(row=6, column=1, padx=10, pady=5)

        # elements in "fourth" column, currently empty
        self.greenhouse_zone_plant_device_details_frame = tk.Frame(self, width=200)
        self.greenhouse_zone_plant_device_details_frame.grid(row=2, column=4, padx=10, pady=5)
