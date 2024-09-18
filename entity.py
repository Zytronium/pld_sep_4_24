from abc import ABC, abstractmethod

from serializer import Serializer


class Entity(ABC):
    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def from_dict(self, data: dict):
        pass

    @abstractmethod
    def save(self, serializer: Serializer, filename: str):
        pass

    @abstractmethod
    def load(self, student_name: str, serializer: Serializer, filename: str):
        pass
