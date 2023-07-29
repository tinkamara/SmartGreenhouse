import tkinter as tk
from tkinter import ttk

class SmartHomeFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # view configuration
        self.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

        # elements in "first" column
        self.room_list_frame = tk.Frame(self, width=200)
        self.room_list_frame.grid(row=1, column=1, padx=10, pady=5, sticky="n")

        self.room_list_frame_label = tk.Label(self.room_list_frame, text="Rooms")
        self.room_list_frame_label.grid(row=1, column=1, sticky="w")

        self.room_listbox = tk.Listbox(self.room_list_frame, width=30, exportselection=False)
        self.room_listbox.grid(row=2, column=2, padx=10, pady=5, rowspan=5)

        self.add_room_button = tk.Button(self.room_list_frame, text="Add Room", width=15)
        self.add_room_button.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.remove_room_button = tk.Button(self.room_list_frame, text="Remove Room", width=15)
        self.remove_room_button.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        # elements in "second" column, currently empty
        self.room_details_frame = tk.Frame(self, width=200)
        self.room_details_frame.grid(row=1, column=2, padx=10, pady=5)

        # elements in "third" column
        self.device_list_frame = tk.Frame(self, width=200)
        self.device_list_frame.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        self.device_list_frame_label = tk.Label(self.device_list_frame, text="Devices")
        self.device_list_frame_label.grid(row=1, column=1, sticky="w")

        self.device_listbox = tk.Listbox(self.device_list_frame, width=30, exportselection=False)
        self.device_listbox.grid(row=2, column=2, padx=10, pady=5, rowspan=5)

        self.remove_device_button = tk.Button(self.device_list_frame, text="Remove Device")
        self.remove_device_button.grid(row=2, column=1, padx=10, pady=5)

        self.device_type_var = tk.StringVar()
        self.device_type_combobox = ttk.Combobox(self.device_list_frame, textvariable=self.device_type_var,
                                                 state="readonly")
        self.device_type_combobox.grid(row=4, column=1, padx=10, pady=5)

        self.add_device_button = tk.Button(self.device_list_frame, text="Add Device")
        self.add_device_button.grid(row=6, column=1, padx=10, pady=5)

        # elements in "fourth" column, currently empty
        self.device_details_frame = tk.Frame(self, width=200)
        self.device_details_frame.grid(row=1, column=4, padx=10, pady=5)
