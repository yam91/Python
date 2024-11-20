from zoo_lion import Lion
from zoo_elephant import Elephant
from zoo_giraff import Giraff
from zoo_visitor import Visitor
import random

lion1 = Lion("Joe", 5, "m")
lion2 = Lion("Leah", 8, "f")
elephant1 = Elephant("Alfi", 7, 200)
elephant2 = Elephant("Hannah", 40, 3000)
giraff1 = Giraff("David", 20, 1800)
giraff2 = Giraff("Shilo", 22, 1000)
visitor1 = Visitor("Dan", 10)
visitor2 = Visitor("Dan's mom", 36)


def twoRandInt(r) :
    arr = [random.randint(0,r), random.randint(0,r)]
    while arr[0] == arr[1]:
        arr[1] = random.randint(0,r)
    return arr


zoo = [lion1, lion2, elephant1, elephant2, giraff1, giraff2, visitor1, visitor2]
intro = [print(f"Hi, my name is {x.name}, I am a {x.age} years old {x.class_name}.") for x in zoo]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in range(7):
    hour = random.randint(0,24)
    print("Now is", hour, "o\'clock on a", days[i])
    Lion.day_count = i % 4
    
    a, b = twoRandInt(len(zoo)-1)
    [partic1, partic2] = [zoo[a], zoo[b]]
    print(partic1.name, partic1.class_name)
    print(partic2.name, partic2.class_name)


    if (partic1.class_name != "Visitor") and (partic2.class_name != "Visitor"):
                partic1.sleep_or_eat(hour)
                partic1.make_sound()
                partic2.sleep_or_eat(hour)
                partic2.make_sound()
                partic1.play(hour, partic2)
    elif (partic1.class_name == "Visitor") and (partic2.class_name == "Visitor"):
            print("We are ", partic1.name, " and ", partic2.name, " visiting the zoo today !")
    else:
        if (partic1.class_name == "Visitor"):
            partic2.sleep_or_eat(hour)
            partic2.make_sound()
            partic1.feed(hour, partic2)
            partic1.play(hour, partic2)                
        else:
            partic1.sleep_or_eat(hour)
            partic1.make_sound()
            partic2.feed(hour, partic1)
            partic2.play(hour,partic1)

                    