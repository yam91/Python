from zoo_animal import Animal

class Carnivore(Animal):
    
    diet = "meat"

    def __init__(self, name, age):
        super().__init__(name, age)

    
    def play(self, t, Animal):
        if self.isSleepEat(t):
             print(f"{self.name} the {self.class_name} is busy now, sorry {Animal.name} the {Animal.class_name} :/")
             return
        if self.isDangerous():
                print(f"{self.name} the {self.class_name}, you are too dangerous to play with {Animal.name} the {Animal.class_name}!")
                return
        return print(f"{self.name} the {self.class_name} and {Animal.name} the {Animal.class_name}, go ahead and play!")

