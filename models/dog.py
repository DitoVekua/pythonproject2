from models.human import Human


class Dog(Human):
    def __init__(self, name, age, leg_count):
        super().__init__(name, age, leg_count)

    def communicate(self):
        print("I am dog,so i can bark")
