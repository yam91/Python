import random

# generate 3 random distinct digits :

def three_distinct_digit(a,b,c):
    while (b==a):
        b = random.randint(0,9)
    while (c==a or c==b):
        c = random.randint(0,9)
    return [a, b, c]


rnd_dig1 = random.randint(1,9)
rnd_dig2 = random.randint(0,9)
rnd_dig3 = random.randint(0,9)

comp_num = three_distinct_digit(rnd_dig1, rnd_dig2,rnd_dig3)

# take user's first guess :
user_input = [int(x) for x in input("Guess a 3 digit number:\n")]

# look for matches :
while (user_input != comp_num):
    isThere = False
    numMatch = 0
    numClose = 0
    for i in range(3):
        if (user_input[i] in comp_num) :
            isThere = True
            if (user_input[i]==comp_num[i]):
                numMatch = numMatch + 1
            else :
                numClose = numClose + 1
        
    if (numMatch) :
        print("Match: you've guessed {n} digit/s correctly.".format(n = numMatch))
        
    if (numClose) :
        print("Close: you've guessed {n} digit/s correctly but in the wrong position.".format(n = numClose))

    if (not isThere):
        print("Nope: You haven't guessed any digit correctly.")
    
    user_input = [int(x) for x in input("Guess again a 3 digit number:\n")]

print("You've successfully guessed the number!")
