from zoo_animal import Animal

class Herbivore(Animal):
    
    diet = "plants"

    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight
    
    def sleep_or_eat(self, t, list):
        if t not in list:
            print(f"{self.name} the {self.class_name}: I am awake and probably eating {self.diet} (my favorite activity), but I am still available for play though ;)")
            return False
        else :
            print(f"{self.name} the {self.class_name}: I am sleeping now for a few hours because now it's night time.")
            return True
        
    def isSleepEat(self, t):
        if t not in self.sleep_inter:
            return False
        else :
            return True

    def isDangerous(self):
        if 200 < self.weight :
            return True
        return False

    def play(self, t, Animal):
        if self.isSleepEat(t):
             print(f"{self.name} the {self.class_name} is busy now, sorry {Animal.name} the {Animal.class_name} :/")
             return
        if Animal.diet == "plants":
            if abs(Animal.weight - self.weight) > 1000:
                print(f"{self.name} the {self.class_name}, it's too dangerous for you to play with {Animal.name} the {Animal.class_name}!")
                return
        elif Animal.isDangerous():
                print(f"{self.name} the {self.class_name}, It's too dangerous, don't play with {Animal.name} the {Animal.class_name}!")
                return
        return print(f"{self.name} the {self.class_name} and {Animal.name} the {Animal.class_name}, go ahead and play!")
