from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self, name):
        self.name = name

    is_alive = True

    @abstractmethod
    def say_hello(self):
        pass

class Student(Human):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am a student')
        return self
    
    def study(self):
        print(f'{self.name} ({self.grade}) is studying')
        return self