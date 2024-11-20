class Visitor:
    class_name = "Visitor"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self, t, Animal):
        if Animal.isDangerous() or self.age < 18 or Animal.isSleepEat(t):
            print(f"{self.name}, please do not play with {Animal.name} the {Animal.class_name}.")
        else:
            print(f"{self.name}, you may play with {Animal.name} the {Animal.class_name}.")
    
    def feed(self, t, Animal):
        if Animal.isSleepEat(t):
            print(f"{self.name}, please do not feed now {Animal.name} the {Animal.class_name}.")
        else:
            print(f"{self.name}, you may feed {Animal.name} the {Animal.class_name}.")
