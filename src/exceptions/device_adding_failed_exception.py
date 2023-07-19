class DeviceAddingFailedException(Exception):

    def __init__(self, device_name: str):
        self.message: str = 'Das Gerät' + device_name + ' ist bereits vorhanden'
        super().__init__(self.message)
