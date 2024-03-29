from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def deliver(self):
        pass
    

class Car(Vehicle):
    
    def __init__(self, model: str):
        self._model = model
    
    def deliver(self):
        return f"Car {self._model} was delivered"
    
    
class Track(Vehicle):
    def __init__(self, model: str):
        self.model = model
        
    def deliver(self):
        return f"Truck {self.model} was delivered"