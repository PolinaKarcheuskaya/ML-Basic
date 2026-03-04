from abc import ABC
from homework_05.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    weight: float
    started: bool
    fuel: float
    fuel_consumption: float

    '''
    Инициализатор
    '''
    def __init__(self, weight:float = 0, fuel:float = 0, fuel_consumption:float = 0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    '''
    Метод запуска двигателя
    '''
    def start(self): 
        if self.started:
            return
        if self.fuel <= 0:
            raise LowFuelError()
        self.started = True

    '''
    Метод расчета необходимого топлива для преодоления дистанции
    '''
    def move(self, distance: float): 
        required_fuel = distance * self.fuel_consumption
        if required_fuel > self.fuel:
            raise NotEnoughFuel()
        self.fuel -= required_fuel


