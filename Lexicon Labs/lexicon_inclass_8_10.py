import functools
dict1 = {'key1' : 1, 'key2' : 2, 'key3': 3}

# With for loop (in class today):
str_rep  = ""
for key, value in dict1.items():
    str_rep += f'{key} = {value}, '
print("With For loop: " + str_rep)

# With list comprehension and join: BESTc
s1 = ", ".join([f'{key} = {value}' for key, value in dict1.items()])
print("With list comprehension and join: " + s1)
# With list comprehension and reduce:
s2 = functools.reduce(lambda x,y: x+y,[f'{key} = {value}, ' for key, value in dict1.items()])
print("With list comprehension and reduce: " + s2)