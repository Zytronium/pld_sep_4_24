#!/bin/bash
import json
from abc import ABC, abstractmethod
from entity import Entity
from serializer import Serializer


class MySerializer(Serializer):
    @staticmethod
    def serialize(data, filename: str):
        with open(filename, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def deserialize(filename: str):
        with open(filename, 'r') as file:
            return json.load(file)

