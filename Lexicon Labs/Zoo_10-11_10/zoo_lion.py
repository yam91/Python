from zoo_carni import Carnivore

class Lion(Carnivore):
# Lions eat every 3-4 days, 6-8 kg for females and 10 kg for males.
# They sleep 15-20 hours mostly through the day.
    class_name = "Lion"
    day_count = 0
    sleep_inter = [x for x in range(6,22)] 

    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.sound = "Rrrrr"
        self.gender = gender
    
    
    def isDangerous(self):
        if self.gender == "m" and 4 <= self.age <= 10 :
            return True
        return False
        
    def sleep_or_eat(self, t):
        if t not in Lion.sleep_inter :
            if not Lion.day_count :
                print(f"{self.name} the {self.class_name}: It's been 3-4 days since I last ate, I am hungry!\nI eat {self.diet}, feed me!")
                return True
            else :
                print(f"{self.name} the {self.class_name}: I am not hungry yet, I will be hungry in 1-2 days.")
                return False
        print(f"{self.name} the {self.class_name}: I am sleeping my beauty sleep now, do not disturb!")
        return True

    def isSleepEat(self, t):
        if t not in Lion.sleep_inter:
                if 3 <= Lion.day_count <= 4 :
                    return True
                else :
                    return False
        return True