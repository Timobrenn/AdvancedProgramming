class Vector:
    def __init__(self,argument):
        self.array = argument
    def __str__(self):
        return f"{self.array}"
from abc import ABC, abstractmethod
class Unit:
        @abstractmethod
        def print_unit(self):
            pass
        @abstractmethod
        def convert_to_is():
            pass
class Velocity(Vector):
    def __init__(self,argument, my_unit="SI"):
        if len(argument) != 3:
            print("not allowed")
        else: 
            super().__init__(argument)
            self.unit= my_unit
    def print_unit(self):
        print(self.unit)

    def convert_to_SI(self):
        if self.unit== "inch/s":
            for i in range (len(self.array)):
                self.array*= 0.0254
v = Velocity ([2,3,4])
print(v)