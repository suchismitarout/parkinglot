from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, veh_num):
        self.veh_num = veh_num

    @abstractmethod
    def vehicle_type(self):
        pass

    def set_veh_num(self, new_veh_num):
        self.veh_num = new_veh_num

    def get_veh_num(self):
        return self.veh_num


class Car(Vehicle):

    def vehicle_type(self):
        return "Car"


class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"
