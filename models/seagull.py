from models.cat import Cat


class Seagull(Cat):
    def __init__(self, name, age, leg_count):
        super().__init__(name, age, leg_count)

    def communicate(self):
        print("I am seagull,so i can fly")

    def can_fly(self):
        return True
