'''
1. Write a program that takes two integers as input, base and exponent, and calculates the power using loops.
2. Write a program that calculates the sum of all elements in a given tuple.
3. Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.
4. Write a program that merges two dictionaries into a single dictionary. If a key is common to both dictionaries, the     value from the second dictionary should be used.
5. Write a program that takes a list of integers as input and uses list comprehension to create a new list containing only the even numbers from the original list.
6. Write a program that takes a string as input and prints its reverse.
'''

# 1.
def exp(base, exponent) :
    result = base
    for i in range(exponent-1):
        result = result*base
    return result

print('the result of 2^2 is: ',exp(2,2))
print('the result of 3^2 is: ', exp(3,2))
print('the result of 3^3 is: ', exp(3,3))

# 2
def sum(tuple) :
    sum = 0
    for i in range(len(tuple)):
        sum = sum + tuple[i]
    return sum

print('the sum of (1,2,3) is: ', sum((1,2,3)))
print('the sum of (4,6,5) is: ', sum((4,6,5)))
print('the sum of (5,5,0) is: ', sum((5,5,0)))

# 3
def even_tuple(tup) :
    arr = []
    for i in range(len(tup)):
        if tup[i]%2==0:
            arr.append(tup[i])
    return tuple(arr)

print('the even numbers in (1, 2, 3) are: ', even_tuple((1,2,3)))
print('the even numbers in (1, 2, 3, 4, 5, 6) are: ', even_tuple((1,2,3,4,5,6)))
print('the even numbers in (12, 22, 33, 44) are: ', even_tuple((12,22,33,44)))

# 4 
dict1 = {'key1' : 1, 
         'key2' : 2,
         'key3' : 3,
         'key4' : 4,
         'key5' : 5}

dict2 = {'key1' : 3, 
         'key2' : 4,
         'key6' : 6,
         'key7' : 7}

def merge_dict(dict1, dict2): 
    for key in dict1:
        if key in dict2 :
            dict1[key] = dict2[key]
    print('dict1 is now: ', dict1)
    return

merge_dict(dict1, dict2)

# 5
def even_list(list):
    evens = []
    for x in list:
        if x%2==0:
            evens.append(x)
    return evens

print('the even numbers in [1, 2, 3] are: ', even_list([1,2,3]))
print('the even numbers in [1, 2, 3, 4, 5, 6] are: ', even_list([1,2,3,4,5,6]))
print('the even numbers in [12, 22, 33, 44] are: ', even_list([12,22,33,44]))

# 6

def revers_str(str):
    rev_str = ''
    for i in range(len(str)):
        rev_str = rev_str + str[len(str)-i-1]
    return rev_str

print('The reversed string of DOG is: ', revers_str('DOG'))
print('The reversed string of CAMEL is: ', revers_str('CAMEL'))
print('The reversed string of LOVE is: ', revers_str('LOVE'))

