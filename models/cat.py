from models.dog import Dog


class Cat(Dog):
    def __init__(self, name, age, leg_count):
        super().__init__(name, age, leg_count)

    def communicate(self):
        print("I am cat,so i can meow")
