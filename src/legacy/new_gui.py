import tkinter as tk
from tkinter import ttk
import os

class SmartGreenhouseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Greenhouse App")

        # Tab-Widget erstellen
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        # Tabs erstellen
        self.smart_home_tab = SmartHomeFrame(self.notebook)
        self.smart_greenhouse_tab = SmartGreenhouseFrame(self.notebook)
        self.plants_tab = PlantsFrame(self.notebook)
        self.log_tab = LogFrame(self.notebook)

        self.notebook.add(self.smart_home_tab, text="Smart Home")
        self.notebook.add(self.smart_greenhouse_tab, text="Smart Greenhouse")
        self.notebook.add(self.plants_tab, text="Plants")
        self.notebook.add(self.log_tab, text="Log")

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

        self.remove_smart_space_button = tk.Button(self.room_list_frame, text="Remove Room", width=15)
        self.remove_smart_space_button.grid(row=6, column=1, padx=10, pady=5, sticky="w")

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

        # set the controller late inside controller's __init__
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

class SmartGreenhouseFrame(ttk.Frame):
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

        self.room_list_frame_label = tk.Label(self.room_list_frame, text="Zones")
        self.room_list_frame_label.grid(row=1, column=1, sticky="w")

        self.room_listbox = tk.Listbox(self.room_list_frame, width=30, exportselection=False)
        self.room_listbox.grid(row=2, column=2, padx=10, pady=5, rowspan=5)

        self.add_room_button = tk.Button(self.room_list_frame, text="Add Zone", width=15)
        self.add_room_button.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.remove_smart_space_button = tk.Button(self.room_list_frame, text="Remove Zone", width=15)
        self.remove_smart_space_button.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        # elements in "second" column, currently empty
        self.room_details_frame = tk.Frame(self, width=200)
        self.room_details_frame.grid(row=1, column=2, padx=10, pady=5)

        # elements in "third" column
        self.device_list_frame = tk.Frame(self, width=200)
        self.device_list_frame.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        self.device_list_frame_label = tk.Label(self.device_list_frame, text="Elements")
        self.device_list_frame_label.grid(row=1, column=1, sticky="w")

        self.device_listbox = tk.Listbox(self.device_list_frame, width=30, exportselection=False)
        self.device_listbox.grid(row=2, column=2, padx=10, pady=5, rowspan=5)

        self.remove_device_button = tk.Button(self.device_list_frame, text="Remove Element")
        self.remove_device_button.grid(row=2, column=1, padx=10, pady=5)

        self.device_type_var = tk.StringVar()
        self.device_type_combobox = ttk.Combobox(self.device_list_frame, textvariable=self.device_type_var,
                                                 state="readonly")
        self.device_type_combobox.grid(row=4, column=1, padx=10, pady=5)

        self.add_device_button = tk.Button(self.device_list_frame, text="Add Element")
        self.add_device_button.grid(row=6, column=1, padx=10, pady=5)

        # elements in "fourth" column, currently empty
        self.device_details_frame = tk.Frame(self, width=200)
        self.device_details_frame.grid(row=1, column=4, padx=10, pady=5)

        # view configuration
        self.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

        # elements in "first" column, second row
        self.room_list_frame = tk.Frame(self, width=200)
        self.room_list_frame.grid(row=1, column=1, padx=10, pady=5, sticky="n")

        self.room_list_frame_label = tk.Label(self.room_list_frame, text="Plants")
        self.room_list_frame_label.grid(row=1, column=1, sticky="w")

        self.room_listbox = tk.Listbox(self.room_list_frame, width=30, exportselection=False)
        self.room_listbox.grid(row=2, column=2, padx=10, pady=5, rowspan=5)

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

        # set the controller late inside controller's __init__
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

class PlantsFrame(ttk.Frame):
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

        self.room_list_frame_label = tk.Label(self.room_list_frame, text="Plants")
        self.room_list_frame_label.grid(row=1, column=1, sticky="w")

        self.room_listbox = tk.Listbox(self.room_list_frame, width=30, exportselection=False)
        self.room_listbox.grid(row=2, column=2, padx=10, pady=5, rowspan=5)

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

        # set the controller late inside controller's __init__
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

class LogFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Log-Textfeld in Log-Frame
        self.filename = "src/legacy/example.log"
        self.last_loaded = 0
        self.log_text = tk.Text(self)
        self.log_text.pack(expand=True, fill='both')
        self.log_text.config(state=tk.DISABLED)  # Deaktiviere Editieren des Textfelds
        self.update_log_text()

    def update_log_text(self):
        try:
            current_modified = os.path.getmtime(self.filename)
            if current_modified != self.last_loaded:
                with open(self.filename, 'r') as file:
                    lines = reversed(file.readlines())
                    content = "\n".join([line.rstrip() for line in lines])
                    self.log_text.config(state=tk.NORMAL)
                    self.log_text.delete("1.0", tk.END)
                    self.log_text.insert(tk.END, content)
                    self.log_text.config(state=tk.DISABLED)
                    self.last_loaded = current_modified
        except:
            pass

        self.after(1000, self.update_log_text)  # Wiederhole die Aktualisierung nach 1 Sekunde
        
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartGreenhouseApp(root)
    root.mainloop()
