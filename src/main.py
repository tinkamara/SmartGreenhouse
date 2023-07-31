from src.entities.layout.greenhouse.greenhouse_model import GreenhouseModel
from src.gui.smart_greenhouse_app import SmartGreenhouseApp
import tkinter as tk

from src.gui.smart_greenhouse_app_controller import SmartGreenhouseAppController
from src.gui.smart_greenhouse_app_view_model import SmartGreenhouseAppViewModel

if __name__=='__main__':
    root = tk.Tk()
    app = SmartGreenhouseApp(root)
    model = SmartGreenhouseAppViewModel(None, None, None)
    controller = SmartGreenhouseAppController(model, app)
    app.set_controller(controller)
    app.update_config()
    root.mainloop()
