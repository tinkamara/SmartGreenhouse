from abc import ABC, abstractmethod


class DeviceView(ABC):

    @abstractmethod
    def __init__(self, model):
        # Initialisiere die View-Komponenten
        pass

    @abstractmethod
    def update_state(self):
        # Aktualisiere die Darstellung basierend auf dem Zustand
        pass
