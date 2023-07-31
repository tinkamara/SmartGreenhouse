import tkinter as tk
from tkinter import simpledialog, messagebox

from src.entities.layout.zone.zone_controller import ZoneController
from src.factorys.plant_factory import PlantFactory
from src.factorys.room_factory import RoomFactory
from src.factorys.zone_factory import ZoneFactory
from src.utilities.config_loader import ConfigLoader


class SmartGreenhouseAppController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.bind_functions_to_view()
        self.config_loader = ConfigLoader()
        self.current_data = self.config_loader.read_config()
        self.set_initial_config()
        self.previous_data = self.current_data.copy()

    def set_initial_config(self):

        # Gib alle Informationen aus der Konfiguration aus
        for room in self.current_data["rooms"]:
            room_controller = RoomFactory.create_room(room["name"], room["ideal_temperature"], room["ideal_air_humidity"])
            self.model.append_room(room_controller.room_model)


        for greenhouse_zone in self.current_data["greenhouse_zones"]:
            zone_controller = ZoneFactory.create_zone(greenhouse_zone["name"], greenhouse_zone["ideal_temperature"], greenhouse_zone["ideal_air_humidity"])
            self.model.append_zone(zone_controller.zone_model)
            print("done")
            for plant in greenhouse_zone["plants"]:
                zone_controller.add_plant(plant["name"], plant["type"], plant["ideal_soil_humidity"], plant["uv_lamp_scale"])
        self.handle_model_change()

    def update_config(self):
        self.current_data = self.config_loader.read_config()
        if self.current_data != self.previous_data:

            if self.previous_data is not None:
                self.compare_configurations()

        # Aktualisiere den gespeicherten Inhalt mit dem aktuellen Inhalt
        self.previous_data = self.current_data.copy()
        self.handle_model_change()

    def compare_configurations(self):
        # Vergleiche die Räume

        # Vergleiche die Räume
        previous_rooms = {room["name"]: room for room in self.previous_data["rooms"]}
        current_rooms = {room["name"]: room for room in self.current_data["rooms"]}

        for room_name, current_room in current_rooms.items():
            if room_name not in previous_rooms:
                zone_controller = ZoneFactory.create_zone(room_name, current_room["ideal_temperature"],
                                                          current_room["ideal_air_humidity"])
                self.model.append_zone(zone_controller.zone_model)


        for room_name, previous_room in previous_rooms.items():
            if room_name not in current_rooms:
                self.model.remove_room(room_name)

        # Vergleiche die Gewächshauszonen
        previous_zones = {zone["name"]: zone for zone in self.previous_data["greenhouse_zones"]}
        current_zones = {zone["name"]: zone for zone in self.current_data["greenhouse_zones"]}

        for zone_name, current_zone in current_zones.items():
            zone_controller: ZoneController = None
            if zone_name not in previous_zones:
                zone_controller = ZoneFactory.create_zone(zone_name, current_zone["ideal_temperature"],
                                                          current_zone["ideal_air_humidity"])
                self.model.append_zone(zone_controller.zone_model)
                for plant in current_zone["plants"]:
                    zone_controller.add_plant(plant["name"], plant["type"], plant["ideal_soil_humidity"],
                                              plant["uv_lamp_scale"])
            else:
                zone_controller = ZoneController.get_zone_controller_by_name(zone_name)
                previous_zone = previous_zones[zone_name]
                self.compare_plants(zone_controller, previous_zone["plants"], current_zone["plants"],
                                    f"Pflanzen in Gewächshauszone '{zone_name}'")

        for zone_name, previous_zone in previous_zones.items():
            if zone_name not in current_zones:
                self.model.remove_zone(zone_name)

    def compare_plants(self, zone_controller, previous_plants, current_plants, heading):
        for plant_name in current_plants:
            if plant_name not in previous_plants:
                current_plant = current_plants[plant_name]
                zone_controller.add_plant(plant_name, current_plant["type"], current_plant["ideal_soil_humidity"], current_plant["uv_lamp_scale"])

        for plant_name in previous_plants:
            if plant_name not in current_plants:
                zone_controller.remove_plant(plant_name)

    def bind_functions_to_view(self):
        # Smart Home Rooms Tab
        self.view.smart_home_tab.room_listbox.bind("<<ListboxSelect>>", self.update_room_details)
        self.view.smart_home_tab.device_listbox.bind("<<ListboxSelect>>", self.update_room_device_details)

        # Smart Greenhouse Zones Tab
        # Row 1: Zones and Zone Devices
        self.view.smart_greenhouse_tab.greenhouse_zone_listbox.bind("<<ListboxSelect>>",
                                                                    self.update_greenhouse_zone_details)
        self.view.smart_greenhouse_tab.greenhouse_zone_device_listbox.bind("<<ListboxSelect>>",
                                                                           self.update_greenhouse_zone_device_details)

        # Row 2: Plants and Plant Devices
        self.view.smart_greenhouse_tab.greenhouse_zone_plant_listbox.bind("<<ListboxSelect>>",
                                                                          self.update_greenhouse_zone_plant_details)
        self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_listbox.bind("<<ListboxSelect>>",
                                                                                 self.update_greenhouse_zone_plant_device_details)

    def update_room_list(self, event=None):
        self.view.smart_home_tab.room_listbox.delete(0, tk.END)
        for room in self.model.rooms:
            self.view.smart_home_tab.room_listbox.insert(tk.END, f"{room.name}")

    def update_room_details(self, event=None):
        selected_index = self.view.smart_home_tab.room_listbox.curselection()
        if not event:
            selected_index = None
        if selected_index:
            selected_room = self.model.rooms[selected_index[0]]
            self.generate_form(self.view.smart_home_tab.room_details_frame, selected_room)
            self.update_room_device_list(selected_room)
        else:
            self.generate_form(self.view.smart_home_tab.room_details_frame)

    def update_room_device_list(self, room=None):
        self.view.smart_home_tab.device_listbox.delete(0, tk.END)
        if room:
            for device in room.devices:
                if not hasattr(device, 'type'):
                    device.type = device.__class__.__name__
                if not hasattr(device, 'name'):
                    device.name = device.type
                self.view.smart_home_tab.device_listbox.insert(tk.END, f"{device.name} <{device.type}>")

    def update_room_device_details(self, event):
        selected_index = self.view.smart_home_tab.room_listbox.curselection()
        if selected_index:
            selected_room = self.model.rooms[selected_index[0]]
            selected_index = self.view.smart_home_tab.device_listbox.curselection()
            if selected_index:
                selected_device = selected_room.devices[selected_index[0]]
                self.generate_form(self.view.smart_home_tab.device_details_frame, selected_device)

    def update_greenhouse_zone_list(self):
        self.view.smart_greenhouse_tab.greenhouse_zone_listbox.delete(0, tk.END)
        for greenhouse_zone in self.model.zones:
            self.view.smart_greenhouse_tab.greenhouse_zone_listbox.insert(tk.END, f"{greenhouse_zone.name}")

    def update_greenhouse_zone_details(self, event=None):
        selected_index = self.view.smart_greenhouse_tab.greenhouse_zone_listbox.curselection()
        if not event:
            selected_index = None
        if selected_index:
            selected_greenhouse_zone = self.model.zones[selected_index[0]]
            self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_details_frame, selected_greenhouse_zone)
            self.update_greenhouse_zone_device_list(selected_greenhouse_zone)
            self.update_greenhouse_zone_plant_list(selected_greenhouse_zone)
        else:
            self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_details_frame)

    def update_greenhouse_zone_device_list(self, greenhouse_zone=None):
        self.view.smart_greenhouse_tab.greenhouse_zone_device_listbox.delete(0, tk.END)
        if greenhouse_zone:
            for device in greenhouse_zone.devices:
                if not hasattr(device, 'type'):
                    device.type = device.__class__.__name__
                if not hasattr(device, 'name'):
                    device.name = device.type
                self.view.smart_greenhouse_tab.greenhouse_zone_device_listbox.insert(tk.END,
                                                                                     f"{device.name} <{device.type}>")

    def update_greenhouse_zone_device_details(self, event):
        selected_index = self.view.smart_greenhouse_tab.greenhouse_zone_listbox.curselection()
        if selected_index:
            selected_greenhouse_zone = self.model.zones[selected_index[0]]
            selected_index = self.view.smart_greenhouse_tab.greenhouse_zone_device_listbox.curselection()
            if selected_index:
                selected_device = selected_greenhouse_zone.devices[selected_index[0]]
                self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_device_details_frame, selected_device)

    def update_greenhouse_zone_plant_list(self, greenhouse_zone=None):
        self.view.smart_greenhouse_tab.greenhouse_zone_plant_listbox.delete(0, tk.END)
        self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_plant_details_frame)
        self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_details_frame)
        self.update_greenhouse_zone_plant_device_list()
        if greenhouse_zone:
            for plant in greenhouse_zone.plants:
                self.view.smart_greenhouse_tab.greenhouse_zone_plant_listbox.insert(tk.END,
                                                                                    f"{plant.name} <{plant.type}>")

    def update_greenhouse_zone_plant_details(self, event):
        selected_index = self.view.smart_greenhouse_tab.greenhouse_zone_listbox.curselection()
        if selected_index:
            selected_greenhouse_zone = self.model.zones[selected_index[0]]
            selected_index = self.view.smart_greenhouse_tab.greenhouse_zone_plant_listbox.curselection()
            if selected_index:
                selected_plant = selected_greenhouse_zone.plants[selected_index[0]]
                self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_plant_details_frame, selected_plant)
                self.update_greenhouse_zone_plant_device_list(selected_plant)

    def update_greenhouse_zone_plant_device_list(self, greenhouse_zone_plant=None):
        self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_listbox.delete(0, tk.END)
        self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_details_frame)
        if greenhouse_zone_plant:
            for device in greenhouse_zone_plant.devices:
                if not hasattr(device, 'type'):
                    device.type = device.__class__.__name__
                if not hasattr(device, 'name'):
                    device.name = device.type
                self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_listbox.insert(tk.END,
                                                                                           f"{device.name} <{device.type}>")

    def update_greenhouse_zone_plant_device_details(self, event):
        selected_zone_index = self.view.smart_greenhouse_tab.greenhouse_zone_listbox.curselection()
        selected_plant_index = self.view.smart_greenhouse_tab.greenhouse_zone_plant_listbox.curselection()
        selected_plant_device_index = self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_listbox.curselection()
        if selected_zone_index and selected_plant_index and selected_plant_device_index:
            greenhouse_zone = self.model.zones[selected_zone_index[0]]
            selected_plant = greenhouse_zone.plants[selected_plant_index[0]]
            selected_plant_device = selected_plant.devices[selected_plant_device_index[0]]
            self.generate_form(self.view.smart_greenhouse_tab.greenhouse_zone_plant_device_details_frame,
                               selected_plant_device)

    def generate_form(self, form_frame, obj=None):
        # empty existing list
        for widget in form_frame.winfo_children():
            widget.destroy()

        if obj == None:
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

            row += 1  # increment row number

    def get_selected_value(self, listbox):
        selected_indices = listbox.curselection()
        if selected_indices:
            # Listbox erlaubt die Mehrfachauswahl, aber in dieser App ist sie deaktiviert.
            index = selected_indices[0]
            selected_value = listbox.get(index)
            return selected_value
        else:
            return None

    def select_element_by_value(self, listbox, value):
        index = None

        for i in range(listbox.size()):
            if listbox.get(i) == value:
                index = i
                break

        if index is not None:
            listbox.selection_set(index)
            listbox.event_generate("<<ListboxSelect>>")  # Manuell das ListboxSelect-Ereignis auslösen

    def handle_model_change(self):

        # Smart Home Tab
        selected_room = self.get_selected_value(self.view.smart_home_tab.room_listbox)
        self.update_room_list()
        self.select_element_by_value(self.view.smart_home_tab.room_listbox, selected_room)
        selected_device = self.get_selected_value(self.view.smart_home_tab.device_listbox)
        self.update_room_device_list()
        self.select_element_by_value(self.view.smart_home_tab.device_listbox, selected_device)

        # Smart Greenhouse Tab
        selected_greenhouse_zone = self.get_selected_value(self.view.smart_greenhouse_tab.greenhouse_zone_listbox)
        self.update_greenhouse_zone_list()
        self.select_element_by_value(self.view.smart_greenhouse_tab.greenhouse_zone_listbox, selected_greenhouse_zone)
        selected_greenhouse_zone_device = self.get_selected_value(
            self.view.smart_greenhouse_tab.greenhouse_zone_listbox)
        self.update_greenhouse_zone_device_list()
        self.select_element_by_value(self.view.smart_greenhouse_tab.greenhouse_zone_listbox,
                                     selected_greenhouse_zone_device)
        selected_greenhouse_zone_plant = self.get_selected_value(self.view.smart_greenhouse_tab.greenhouse_zone_listbox)
        self.update_greenhouse_zone_plant_list()
        self.select_element_by_value(self.view.smart_greenhouse_tab.greenhouse_zone_listbox,
                                     selected_greenhouse_zone_plant)
        selected_greenhouse_zone_plant_device = self.get_selected_value(
            self.view.smart_greenhouse_tab.greenhouse_zone_listbox)
        self.update_greenhouse_zone_plant_device_list()
        self.select_element_by_value(self.view.smart_greenhouse_tab.greenhouse_zone_listbox,
                                     selected_greenhouse_zone_plant_device)
