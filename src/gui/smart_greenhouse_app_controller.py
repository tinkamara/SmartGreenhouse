import tkinter as tk
from tkinter import simpledialog, messagebox

class Room:
    def __init__(self, name):
        self.name = name
        self.devices = []

class GreenhouseZone:
    def __init__(self, name):
        self.name = name
        self.devices = []
        self.plants = []

class SmartHomeAppController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.bind_functions_to_view()

    def bind_functions_to_view(self):
        # Smart Home Rooms Tab
        self.view.smart_home_tab.room_listbox.bind("<<ListboxSelect>>", self.update_room_details)
        self.view.smart_home_tab.add_room_button.config(command=self.add_room)
        self.view.smart_home_tab.remove_room_button.config(command=self.remove_room)
        self.view.smart_home_tab.device_listbox.bind("<<ListboxSelect>>", self.update_room_device_details)
        self.view.smart_home_tab.add_room_device_button.config(command=self.add_room_device)
        self.view.smart_home_tab.remove_room_device_button.config(command=self.remove_room_device)
        
        # Smart Greenhouse Zones Tab
        # Row 1: Zones and Zone Devices
        self.view.smart_home_tab.greenhouse_zone_listbox.bind("<<ListboxSelect>>", self.update_greenhouse_zone_details)
        self.view.smart_home_tab.add_greenhouse_zone_button.config(command=self.add_greenhouse_zone)
        self.view.smart_home_tab.remove_greenhouse_zone_button.config(command=self.remove_greenhouse_zone)
        self.view.smart_home_tab.device_listbox.bind("<<ListboxSelect>>", self.update_greenhouse_zone_device_details)
        self.view.smart_home_tab.add_greenhouse_zone_device_button.config(command=self.add_greenhouse_zone_device)
        self.view.smart_home_tab.remove_greenhouse_zone_device_button.config(command=self.remove_greenhouse_zone_device)
        # Row 2: Plants and Plant Devices
        self.view.smart_home_tab.greenhouse_zone_plant_listbox.bind("<<ListboxSelect>>", self.update_greenhouse_zone_plant_details)
        self.view.smart_home_tab.add_greenhouse_zone_plant_button.config(command=self.add_greenhouse_zone_plant)
        self.view.smart_home_tab.remove_greenhouse_zone_plant_button.config(command=self.remove_greenhouse_zone_plant)
        self.view.smart_home_tab.device_listbox.bind("<<ListboxSelect>>", self.update_greenhouse_zone_plant_device_details)
        self.view.smart_home_tab.add_greenhouse_zone_plant_device_button.config(command=self.add_greenhouse_zone_plant_device)
        self.view.smart_home_tab.remove_greenhouse_zone_plant_device_button.config(command=self.remove_greenhouse_zone_plant_device)

    def add_room(self):
        room_name = simpledialog.askstring("New Room", "Enter the name for the new room:")
        if room_name:
            if not self.room_name_exists(room_name):
                self.model.rooms.append(Room(room_name))
                self.view.smart_home_tab.room_listbox.insert(tk.END, f"{room_name}")

    def room_name_exists(self, new_room_name):
        for room in self.model.rooms:
            if room.name == new_room_name:
                messagebox.showerror("Error",
                                     f"A room called \"{new_room_name}\" already exists!")
                return True
        return False

    def remove_room(self):
        selected_index = self.view.smart_home_tab.room_listbox.curselection()
        if selected_index:
            selected_room = self.model.rooms[selected_index[0]]
            self.model.rooms.remove(selected_room)
            self.view.smart_home_tab.room_listbox.delete(selected_index[0])
            self.update_room_details()


    def update_room_details(self, event=None):
        selected_index = self.view.smart_home_tab.room_listbox.curselection()
        if not event:
            selected_index = None
        if selected_index:
            selected_room = self.model.rooms[selected_index[0]]
            self.generate_form(self.view.smart_home_tab.room_details_frame, selected_room)
            self.update_room_device_list(selected_room)
            self.update_room_device_type_combobox(selected_room)
        else:
            self.generate_form(self.view.smart_home_tab.room_details_frame)
            self.update_room_device_type_combobox()

    def update_room_device_list(self, room=None):
        self.view.smart_home_tab.device_listbox.delete(0, tk.END)
        if room:
            for device in room.devices:
                self.view.smart_home_tab.device_listbox.insert(tk.END, f"{device.name} <{device.type}>")

    def update_room_device_type_combobox(self, room=None):
        device_types = None
        if room:
            device_types = list(room.get_available_device_dict().keys())
        if device_types:
            self.view.smart_home_tab.device_type_combobox["values"] = device_types
            self.view.smart_home_tab.device_type_combobox.current(0)
        else:
            self.view.smart_home_tab.device_type_combobox["values"] = []
            self.view.smart_home_tab.device_type_combobox.set('')
            self.update_room_device_list()
            self.generate_form(self.view.smart_home_tab.device_details_frame)

    def add_room_device(self):
        selected_index = self.view.smart_home_tab.room_listbox.curselection()
        if selected_index:
            room = self.model.rooms[selected_index[0]]
            device_name = simpledialog.askstring("New Device", "Enter a name for your new device:")

            if device_name:
                for device in room.devices:
                    if device.name == device_name:
                        messagebox.showerror("Error",
                                             f"The {room.type} \"{room.name}\" already possesses "
                                             f"a {device.type} named {device_name}!")
                        return

                device_type = self.view.smart_home_tab.device_type_combobox.get()
                device_type_dict = room.get_available_device_dict()
                if device_type in device_type_dict.keys():
                    if room.add_room_device(device_type_dict[device_type], device_name):
                        self.update_room_device_list(room)
                else:
                    messagebox.showerror("Error", f"This type of device cannot be added to the"
                                                  f"{room.type} \"{room.name}\"")

    def remove_room_device(self):
        selected_index = self.view.smart_home_tab.device_listbox.curselection()
        if selected_index:
            selected_device = self.view.smart_home_tab.device_listbox.get(selected_index[0])
            selected_room_index = self.view.smart_home_tab.room_listbox.curselection()[0]
            selected_room = self.model.rooms[selected_room_index]

            for device in selected_room.devices:
                if device.name + f" <{device.type}>" == selected_device:
                    selected_room.devices.remove(device)
                    self.view.smart_home_tab.device_listbox.delete(selected_index[0])
                    self.generate_form(self.view.smart_home_tab.device_details_frame)
                    break

    def update_room_device_details(self, event):
        selected_index = self.view.smart_home_tab.room_listbox.curselection()
        if selected_index:
            selected_room = self.model.rooms[selected_index[0]]
            selected_index = self.view.smart_home_tab.device_listbox.curselection()
            if selected_index:
                selected_device = selected_room.devices[selected_index[0]]
                self.generate_form(self.view.smart_home_tab.device_details_frame, selected_device)

    def add_greenhouse_zone(self):
        greenhouse_zone_name = simpledialog.askstring("New Greenhouse Zone", "Enter the name for the new greenhouse_zone:")
        if greenhouse_zone_name:
            if not self.greenhouse_zone_name_exists(greenhouse_zone_name):
                self.model.greenhouse_zones.append(GreenhouseZone(greenhouse_zone_name))
                self.view.smart_greenhouse_tab.greenhouse_zone_listbox.insert(tk.END, f"{greenhouse_zone_name}")

    def greenhouse_zone_name_exists(self, new_greenhouse_zone_name):
        for greenhouse_zone in self.model.greenhouse_zones:
            if greenhouse_zone.name == new_greenhouse_zone_name:
                messagebox.showerror("Error",
                                     f"A greenhouse zone called \"{new_greenhouse_zone_name}\" already exists!")
                return True
        return False

    def remove_greenhouse_zone(self):
        selected_index = self.view.smart_greenhouse_tab.greenhouse_zone_listbox.curselection()
        if selected_index:
            selected_greenhouse_zone = self.model.greenhouse_zones[selected_index[0]]
            self.model.greenhouse_zones.remove(selected_greenhouse_zone)
            self.view.smart_greenhouse_tab.greenhouse_zone_listbox.delete(selected_index[0])
            self.update_greenhouse_zone_details()

    def update_greenhouse_zone_details(self, event=None):
        selected_index = self.view.smart_greenhouse_tab.greenhouse_zone_listbox.curselection()
        if not event:
            selected_index = None
        if selected_index:
            selected_greenhouse_zone = self.model.greenhouse_zones[selected_index[0]]
            self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_details_frame, selected_greenhouse_zone)
            self.update_greenhouse_zone_device_list(selected_greenhouse_zone)
            self.update_greenhouse_zone_device_type_combobox(selected_greenhouse_zone)
            self.update_greenhouse_zone_plant_list(selected_greenhouse_zone)
            self.update_greenhouse_zone_plant_type_combobox(selected_greenhouse_zone)
            self.update_greenhouse_zone_plant_device_list(selected_greenhouse_zone)
            self.update_greenhouse_zone_plant_device_type_combobox(selected_greenhouse_zone)
        else:
            self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_details_frame)
            self.update_greenhouse_zone_device_type_combobox()
            self.update_greenhouse_zone_plant_type_combobox()
            self.update_greenhouse_zone_plant_device_type_combobox()

    def update_greenhouse_zone_device_list(self, greenhouse_zone=None):
        self.view.smart_greenhouse_tab.device_listbox.delete(0, tk.END)
        if greenhouse_zone:
            for device in greenhouse_zone.devices:
                self.view.smart_greenhouse_tab.device_listbox.insert(tk.END, f"{device.name} <{device.type}>")

    def update_greenhouse_zone_device_type_combobox(self, greenhouse_zone=None):
        device_types = None
        if greenhouse_zone:
            device_types = list(greenhouse_zone.get_available_device_dict().keys())
        if device_types:
            self.view.smart_greenhouse_tab.device_type_combobox["values"] = device_types
            self.view.smart_greenhouse_tab.device_type_combobox.current(0)
        else:
            self.view.smart_greenhouse_tab.device_type_combobox["values"] = []
            self.view.smart_greenhouse_tab.device_type_combobox.set('')
            self.update_greenhouse_zone_device_list()
            self.generate_form(self.view.smart_greenhouse_tab.device_details_frame)

    def add_greenhouse_zone_device(self):
        selected_index = self.view.smart_greenhouse_tab.greenhouse_zone_listbox.curselection()
        if selected_index:
            greenhouse_zone = self.model.greenhouse_zones[selected_index[0]]
            device_name = simpledialog.askstring("New Device", "Enter a name for your new device:")

            if device_name:
                for device in greenhouse_zone.devices:
                    if device.name == device_name:
                        messagebox.showerror("Error",
                                             f"The {greenhouse_zone.type} \"{greenhouse_zone.name}\" already possesses "
                                             f"a {device.type} named {device_name}!")
                        return

                device_type = self.view.smart_greenhouse_tab.device_type_combobox.get()
                device_type_dict = greenhouse_zone.get_available_device_dict()
                if device_type in device_type_dict.keys():
                    if greenhouse_zone.add_greenhouse_zone_device(device_type_dict[device_type], device_name):
                        self.update_greenhouse_zone_device_list(greenhouse_zone)
                else:
                    messagebox.showerror("Error", f"This type of device cannot be added to the"
                                                  f"{greenhouse_zone.type} \"{greenhouse_zone.name}\"")

    def remove_greenhouse_zone_device(self):
        selected_index = self.view.smart_greenhouse_tab.device_listbox.curselection()
        if selected_index:
            selected_device = self.view.smart_greenhouse_tab.device_listbox.get(selected_index[0])
            selected_greenhouse_zone_index = self.view.smart_greenhouse_tab.greenhouse_zone_listbox.curselection()[0]
            selected_greenhouse_zone = self.model.greenhouse_zones[selected_greenhouse_zone_index]

            for device in selected_greenhouse_zone.devices:
                if device.name + f" <{device.type}>" == selected_device:
                    selected_greenhouse_zone.devices.remove(device)
                    self.view.smart_greenhouse_tab.device_listbox.delete(selected_index[0])
                    self.generate_form(self.view.smart_greenhouse_tab.device_details_frame)
                    break

    def update_greenhouse_zone_device_details(self, event):
        selected_index = self.view.smart_greenhouse_tab.greenhouse_zone_listbox.curselection()
        if selected_index:
            selected_greenhouse_zone = self.model.greenhouse_zones[selected_index[0]]
            selected_index = self.view.smart_greenhouse_tab.device_listbox.curselection()
            if selected_index:
                selected_device = selected_greenhouse_zone.devices[selected_index[0]]
                self.generate_form(self.view.smart_greenhouse_tab.device_details_frame, selected_device)

    def update_greenhouse_zone_plant_list(self, greenhouse_zone=None):
        self.view.smart_greenhouse_tab.greenhouse_zone_plant_listbox.delete(0, tk.END)
        self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_plant_details_frame)
        self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_details_frame)
        self.update_greenhouse_zone_plant_device_list()
        if greenhouse_zone:
            for plant in greenhouse_zone.plants:
                self.view.smart_greenhouse_tab.greenhouse_zone_plant_listbox.insert(tk.END, f"{plant.name} <{plant.type}>")

    def update_greenhouse_zone_plant_type_combobox(self, greenhouse_zone=None):
        plant_types = None
        if greenhouse_zone:
            plant_types = list(greenhouse_zone.get_available_plant_dict().keys())
        if plant_types:
            self.view.smart_greenhouse_tab.greenhouse_zone_plant_type_combobox["values"] = plant_types
            self.view.smart_greenhouse_tab.greenhouse_zone_plant_type_combobox.current(0)
        else:
            self.view.smart_greenhouse_tab.greenhouse_zone_plant_type_combobox["values"] = []
            self.view.smart_greenhouse_tab.greenhouse_zone_plant_type_combobox.set('')
            self.update_greenhouse_zone_plant_list()
            self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_plant_details_frame)

    def add_greenhouse_zone_plant(self):
        selected_index = self.view.smart_greenhouse_tab.greenhouse_zone_listbox.curselection()
        if selected_index:
            greenhouse_zone = self.model.greenhouse_zones[selected_index[0]]
            plant_name = simpledialog.askstring("New plant", "Enter a name for your new plant:")

            if plant_name:
                for plant in greenhouse_zone.plants:
                    if plant.name == plant_name:
                        messagebox.showerror("Error",
                                             f"The {greenhouse_zone.type} \"{greenhouse_zone.name}\" already possesses "
                                             f"a {plant.type} named {plant_name}!")
                        return

                plant_type = self.view.smart_greenhouse_tab.greenhouse_zone_plant_type_combobox.get()
                plant_type_dict = greenhouse_zone.get_available_plant_dict()
                if plant_type in plant_type_dict.keys():
                    if greenhouse_zone.add_greenhouse_zone_plant(plant_type_dict[plant_type], plant_name):
                        self.update_greenhouse_zone_plant_list(greenhouse_zone)
                else:
                    messagebox.showerror("Error", f"This type of plant cannot be added to the"
                                                  f"{greenhouse_zone.type} \"{greenhouse_zone.name}\"")

    def remove_greenhouse_zone_plant(self):
        selected_index = self.view.smart_greenhouse_tab.greenhouse_zone_plant_listbox.curselection()
        if selected_index:
            selected_plant = self.view.smart_greenhouse_tab.greenhouse_zone_plant_listbox.get(selected_index[0])
            selected_greenhouse_zone_index = self.view.smart_greenhouse_tab.greenhouse_zone_listbox.curselection()[0]
            selected_greenhouse_zone = self.model.greenhouse_zones[selected_greenhouse_zone_index]
            selected_greenhouse_zone.remove(selected_plant)
            self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_plant_details_frame)
            self.update_greenhouse_zone_plant_device_list()

    def update_greenhouse_zone_plant_details(self, event):
        selected_index = self.view.smart_greenhouse_tab.greenhouse_zone_listbox.curselection()
        if selected_index:
            selected_greenhouse_zone = self.model.greenhouse_zones[selected_index[0]]
            selected_index = self.view.smart_greenhouse_tab.greenhouse_zone_plant_listbox.curselection()
            if selected_index:
                selected_plant = selected_greenhouse_zone.plants[selected_index[0]]
                self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_plant_details_frame, selected_plant)
    
    def update_greenhouse_zone_plant_device_list(self, greenhouse_zone_plant=None):
        self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_listbox.delete(0, tk.END)
        self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_plant_details_frame)
        if greenhouse_zone_plant:
            for device in greenhouse_zone_plant.devices:
                self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_listbox.insert(tk.END, f"{device.name} <{device.type}>")

    def update_greenhouse_zone_plant_device_type_combobox(self, greenhouse_zone_plant=None):
        device_types = None
        if greenhouse_zone_plant:
            device_types = list(greenhouse_zone_plant.get_available_plant_dict().keys())
        if device_types:
            self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_type_combobox["values"] = device_types
            self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_type_combobox.current(0)
        else:
            self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_type_combobox["values"] = []
            self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_type_combobox.set('')
            self.update_greenhouse_zone_plant_device_list()
            self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_details_frame)

    def add_greenhouse_zone_plant_device(self):
        selected_zone_index = self.view.smart_greenhouse_tab.greenhouse_zone_listbox.curselection()
        selected_plant_index = self.view.smart_greenhouse_tab.greenhouse_zone_plant_listbox.curselection()
        if selected_zone_index and selected_plant_index:
            greenhouse_zone = self.model.greenhouse_zones[selected_zone_index[0]]
            selected_plant = greenhouse_zone.plants[selected_plant_index[0]]
            plant_device_name = simpledialog.askstring("New plant", "Enter a name for your new plant:")

            if plant_device_name:
                for device in selected_plant:
                    if device.name == plant_device_name:
                        messagebox.showerror("Error",
                                             f"The {greenhouse_zone.type} \"{greenhouse_zone.name}\" already possesses "
                                             f"a {device.type} named {plant_device_name}!")
                        return

                plant_device_type = self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_type_combobox.get()
                plant_device_type_dict = selected_plant.get_available_device_dict()
                if plant_device_type in plant_device_type_dict.keys():
                    if greenhouse_zone.add_greenhouse_zone_plant_device(plant_device_type_dict[plant_device_type], plant_device_name):
                        self.update_greenhouse_zone_plant_device_list(greenhouse_zone)
                else:
                    messagebox.showerror("Error", f"This type of device cannot be added to the"
                                                  f"{selected_plant.type} \"{selected_plant.name}\"")

    def remove_greenhouse_zone_plant_device(self):
        selected_zone_index = self.view.smart_greenhouse_tab.greenhouse_zone_listbox.curselection()
        selected_plant_index = self.view.smart_greenhouse_tab.greenhouse_zone_plant_listbox.curselection()
        selected_plant_device_index = self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_listbox.curselection()
        if selected_zone_index and selected_plant_index and selected_plant_device_index:
            greenhouse_zone = self.model.greenhouse_zones[selected_zone_index[0]]
            selected_plant = greenhouse_zone.plants[selected_plant_index[0]]
            selected_plant_device = selected_plant.devices[selected_plant_device_index[0]]
            selected_plant.devices.remove(selected_plant_device)
            self.update_greenhouse_zone_plant_device_list(selected_plant)
            self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_details_frame)

    def update_greenhouse_zone_plant_device_details(self, event):
        selected_zone_index = self.view.smart_greenhouse_tab.greenhouse_zone_listbox.curselection()
        selected_plant_index = self.view.smart_greenhouse_tab.greenhouse_zone_plant_listbox.curselection()
        selected_plant_device_index = self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_listbox.curselection()
        if selected_zone_index and selected_plant_index and selected_plant_device_index:
            greenhouse_zone = self.model.greenhouse_zones[selected_zone_index[0]]
            selected_plant = greenhouse_zone.plants[selected_plant_index[0]]
            selected_plant_device = selected_plant.devices[selected_plant_device_index[0]]
            self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_details_frame, selected_plant_device)
    
    def generate_form(self, form_frame, obj=None):
        # empty existing list
        for widget in form_frame.winfo_children():
            widget.destroy()

        if obj==None:
            return

        label_vars = {}  # dictionary for saving label variables

        row = 0  # row number for placement inside the widget

        for attr, value in obj.__dict__.items():
            if attr in self.model.hidden_attributes:
                continue
            label_text = self.model.attribute_labels.get(attr, attr)
            label_var = tk.StringVar(value=f"{label_text}:")
            label = tk.Label(form_frame, textvariable=label_var, anchor="w")
            label.grid(row=row, column=0, sticky="w", padx=10, pady=5)
            label_vars[attr] = label_var

            if isinstance(value, bool):
                value_text = "True" if value else "False"
            else:
                value_text = str(value)

            value_var = tk.StringVar(value=value_text)
            value_label = tk.Label(form_frame, textvariable=value_var, anchor="e")
            value_label.grid(row=row, column=1, sticky="e", padx=10, pady=5)

            if attr in self.model.no_change_attributes:
                row += 1
                continue

            if isinstance(value, bool):
                def toggle_boolean_attribute(attribute):
                    obj.__dict__[attribute] = not obj.__dict__[attribute]
                    label_vars[attribute].set(f"{label_text}:")
                    value_var.set("True" if obj.__dict__[attribute] else "False")
                    self.generate_form(form_frame, obj)

                button = tk.Button(form_frame, text="Change", command=lambda attr=attr: toggle_boolean_attribute(attr))
                button.grid(row=row, column=2, sticky="e", padx=10, pady=5)

            elif isinstance(value, (str, int)):
                def update_string_or_integer_attribute(attribute):
                    new_value = simpledialog.askstring("Change Attribute", f"Enter new value for {label_text}",
                                                       initialvalue=obj.__dict__[attribute])
                    if new_value is not None:
                        if isinstance(obj.__dict__[attribute], int):
                            new_value = int(new_value)
                        obj.__dict__[attribute] = new_value
                        label_vars[attribute].set(f"{label_text}:")
                        value_var.set(str(obj.__dict__[attribute]))
                        self.generate_form(form_frame, obj)

                button = tk.Button(form_frame, text="Change",
                                   command=lambda attr=attr: update_string_or_integer_attribute(attr))
                button.grid(row=row, column=2, sticky="e", padx=10, pady=5)

            row += 1  # increment row number
