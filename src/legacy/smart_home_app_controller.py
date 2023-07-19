import tkinter as tk
from tkinter import simpledialog, messagebox


class SmartHomeAppController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.bind_functions_to_view()

    def bind_functions_to_view(self):
        self.view.room_listbox.bind("<<ListboxSelect>>", self.update_room_details)
        self.view.add_room_button.config(command=self.add_room)
        self.view.add_sig_button.config(command=self.add_sig)
        self.view.remove_smart_space_button.config(command=self.remove_smart_space)
        self.view.device_listbox.bind("<<ListboxSelect>>", self.update_device_details)
        self.view.add_device_button.config(command=self.add_device)
        self.view.remove_device_button.config(command=self.remove_device)

    def add_room(self):
        room_name = simpledialog.askstring("New Room", "Enter the name for the new room:")
        if room_name:
            if not self.smart_space_name_exists(room_name):
                room = 'bla'
                self.model.smart_spaces.append(room)
                self.view.room_listbox.insert(tk.END, f"{room_name} <{room.type}>")

    def smart_space_name_exists(self, new_smart_space_name):
        for smart_space in self.model.smart_spaces:
            if smart_space.name == new_smart_space_name:
                messagebox.showerror("Error",
                                     f"A {smart_space.type} has already been given the name {new_smart_space_name}!")
                return True
        return False

    def remove_smart_space(self):
        selected_index = self.view.room_listbox.curselection()
        if selected_index:
            selected_room = self.model.smart_spaces[selected_index[0]]
            self.model.smart_spaces.remove(selected_room)
            self.view.room_listbox.delete(selected_index[0])
            self.update_room_details()


    def update_room_details(self, event=None):
        selected_index = self.view.room_listbox.curselection()
        if not event:
            selected_index = None
        if selected_index:
            selected_room = self.model.smart_spaces[selected_index[0]]
            self.generate_form(self.view.room_details_frame, selected_room)
            self.update_device_list(selected_room)
            self.update_device_type_combobox(selected_room)
        else:
            self.generate_form(self.view.room_details_frame)
            self.update_device_type_combobox()

    def update_device_list(self, smart_space=None):
        self.view.device_listbox.delete(0, tk.END)
        if smart_space:
            for device in smart_space.devices:
                self.view.device_listbox.insert(tk.END, f"{device.name} <{device.type}>")

    def update_device_type_combobox(self, smart_space=None):
        device_types = None
        if smart_space:
            device_types = list(smart_space.get_available_device_dict().keys())
        if device_types:
            self.view.device_type_combobox["values"] = device_types
            self.view.device_type_combobox.current(0)
        else:
            self.view.device_type_combobox["values"] = []
            self.view.device_type_combobox.set('')
            self.update_device_list()
            self.generate_form(self.view.device_details_frame)

    def add_device(self):
        selected_index = self.view.room_listbox.curselection()
        if selected_index:
            smart_space = self.model.smart_spaces[selected_index[0]]
            device_name = simpledialog.askstring("New Device", "Enter a name for your new device:")

            if device_name:
                for device in smart_space.devices:
                    if device.name == device_name:
                        messagebox.showerror("Error",
                                             f"The {smart_space.type} \"{smart_space.name}\" already possesses "
                                             f"a {device.type} named {device_name}!")
                        return

                device_type = self.view.device_type_combobox.get()
                device_type_dict = smart_space.get_available_device_dict()
                if device_type in device_type_dict.keys():
                    if smart_space.add_device(device_type_dict[device_type], device_name):
                        self.update_device_list(smart_space)
                else:
                    messagebox.showerror("Error", f"This type of device cannot be added to the"
                                                  f"{smart_space.type} \"{smart_space.name}\"")

    def remove_device(self):
        selected_index = self.view.device_listbox.curselection()
        if selected_index:
            selected_device = self.view.device_listbox.get(selected_index[0])
            selected_smart_space_index = self.view.room_listbox.curselection()[0]
            selected_smart_space = self.model.smart_spaces[selected_smart_space_index]

            for device in selected_smart_space.devices:
                if device.name + f" <{device.type}>" == selected_device:
                    selected_smart_space.devices.remove(device)
                    self.view.device_listbox.delete(selected_index[0])
                    self.generate_form(self.view.device_details_frame)
                    break

    def update_device_details(self, event):
        selected_index = self.view.room_listbox.curselection()
        if selected_index:
            selected_room = self.model.smart_spaces[selected_index[0]]
            selected_index = self.view.device_listbox.curselection()
            if selected_index:
                selected_device = selected_room.devices[selected_index[0]]
                self.generate_form(self.view.device_details_frame, selected_device)

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

                if attr in self.model.no_change_attributes:
                    row += 1
                    continue

                button = tk.Button(form_frame, text="Change",
                                   command=lambda attr=attr: update_string_or_integer_attribute(attr))
                button.grid(row=row, column=2, sticky="e", padx=10, pady=5)

            row += 1  # increment row number
