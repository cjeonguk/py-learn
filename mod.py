class Human:
    def __init__(self, name):
        self.name = name

    is_alive = True

    def say_hello(self):
        print(f'Hello, my name is {self.name}')


class Student(Human):
    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am a student')
        return self
    
    def study(self):
        print(f'{self.name} is studying')
        return self