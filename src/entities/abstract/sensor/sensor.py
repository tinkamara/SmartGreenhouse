from abc import abstractmethod, ABC


class Sensor(ABC):

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def lower_value(self, value):
        pass

    @abstractmethod
    def raise_value(self, value):
        pass

    @abstractmethod
    def random_value_change(self, value):
        pass
