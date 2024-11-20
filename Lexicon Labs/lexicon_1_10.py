#ex.1
s = 'Python'

print(s[4]) #'o'
print(s[:-2]) #'Pyth'
print(s[1:-2]) #'yth'
print(s[::-1]) #'Pyth'

#ex.2
I = [3, 7, [1,4,'hello']]
print(I)

I[2][2] = "goodbye"
print(I)

#ex.3
d1 = {'simple_key': 'hello'}
d2 = {'k1': {'k2' : 'hello'}}
d3 = {'k1': [{'nest_key': ['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

#ex.4
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

myset = {x for x in mylist}
print(myset)

#ex.5
age = 4
name = "Sammy"

print("Hello my dog's name is {n} and he is {a} years old.".format(n = name, a=age))