from abc import ABC, abstractmethod

class Serializer(ABC):
    @abstractmethod
    def serialize(self, data, filename: str):
        pass

    @abstractmethod
    def deserialize(self, filename: str):
        pass
