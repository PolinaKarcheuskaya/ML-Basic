"""
Класс `Car`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.engine import Engine

class Car(Vehicle):
    engine: Engine

    def __init__(self, weight: float = 0, fuel: float = 0, fuel_consumption: float = 0, engine: Engine = None):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, engine: Engine):
        self.engine = engine