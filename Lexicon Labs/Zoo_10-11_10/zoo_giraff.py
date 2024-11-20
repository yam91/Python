from zoo_herbi import Herbivore

class Giraff(Herbivore):
# a giraff sleeps for something like 4.5 hours a day, usually at night ->
# let's say then it sleeps from midnight to 4:30 in the morning.
# It eats most of the day ->
# let's say 24 - 4.5 (sleep time) - 2 (random guess) =  17.5 hours of the day.
# It eats 34 kg per day.
    class_name = "Giraff"
    sleep_inter = [x for x in range(0, 5)]

    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.sound = "Sssssss"

    def sleep_or_eat(self, t):
        super().sleep_or_eat(t, Giraff.sleep_inter)
    
    def isDangerous(self):
        super().isDangerous()

    def play(self, t, Animal):
        super().play(t, Animal)