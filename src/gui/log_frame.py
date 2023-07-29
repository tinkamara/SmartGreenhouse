import tkinter as tk
from tkinter import ttk
import os

class LogFrame(ttk.Frame):
    def __init__(self, parent, filename=""):
        super().__init__(parent)
        
        # Log-Textfeld in Log-Frame
        self.filename = filename
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
