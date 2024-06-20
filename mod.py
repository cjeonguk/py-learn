class Human:
    def __init__(self, name):
        self.name = name

    is_alive = True

    def say_hello(self):
        print(f'Hello, my name is {self.name}')


class Student(Human):
    pass