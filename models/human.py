from models.animal import Animal


class Human(Animal):
    def __init__(self, name, age, leg_count):
        super().__init__(name, age, leg_count)

    def to_string(self):
        d = dict()
        d['Name'] = self.name
        d['Age'] = self.age
        d['Leg_Count'] = self.leg_count
        return d

    def communicate(self):
        print("I am human,so i can talk")

    def can_fly(self):
        return False
