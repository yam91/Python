from zoo_herbi import Herbivore

class Elephant(Herbivore):
# Elephants eat 150 kg per day for 18 hours.
# They sleep 4-6 hours per day mainly at night.
    class_name = "Elephant"
    sleep_inter = [x for x in range(0, 6)]

    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.sound = "Truuuu"

    
    def sleep_or_eat(self, t):
        super().sleep_or_eat(t, Elephant.sleep_inter)

    def isDangerous(self):
        super().isDangerous()

    def play(self, t, Animal):
        super().play(t, Animal)
