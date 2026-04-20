
"""
Abstract Base Classes (ABCs) in Python serve as a design pattern for creating templates or 
blueprints for other classes to inherit from, characterized by two primary constraints:
* Instance Prevention: Consumers are restricted from creating instances of the base class 
                    itself, as its purpose is solely to serve as a blueprint or a collection 
                    of common attributes.
* Method Enforcement: ABCs allow developers to enforce a constraint that specific methods 
                    defined in the base class must be implemented by any inheriting subclasses.
"""
from abc import ABC, abstractmethod

# Using Abstract Base classes to enforce class constraints

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def calcArea(self):
        print("calcArea passed")
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    
    def calcArea(self):
        return self.side * self.side


c = Circle(10)
print(c.calcArea())

s = Square(4)
print(s.calcArea())