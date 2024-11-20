'''
1. Lambda functions:
- A Lambda function is a function defined "on the spot" where it is passed as a parameter 
to higher order functions (functions which can take functions) or where it used to define
a variable. It is nameless and usually executes simple and concise operations.

Lambda functions are faster than regular functions because they are defined and passed in 
one single step, unlike regular functions which are defined and passed separately (see below).

It has a slightly different syntax compared to the regular def of functions:
'''

# Regular function:
def double(list):
    new_list = []
    for x in list:
        new_list.append(x*2)
    return new_list

myList = [1,2,3]
print("Mylist is: ", myList)
print("Doubling myList with a regular function: ", double(myList))

# With map():
print("Doubling myList with a lambda passed to a map function: ", list(map(lambda x : x*2, myList)))

# In a Variable:
db = lambda x: x*2
print("Doubling myList with a lambda defined as a variable passed to a map function: ",list(map(db, myList)))


'''
- Lambda functions are useful when dealing with short operations, as "one-off" functions - 
a one-time only functions or as parameters for higher order functions (such as map(), 
filter() etc.)

- A Lambda function is also called an anonymous function, because it is nameless,
unlike a regular function which is named when defined. 
An inline function is a function that has less so-called overhead of passing parameters 
between caller and callee. Lambda functions are a type of inline funtions.


2. The filter function:

The filter function takes a filter function/condition and an iterable, e.g. list, to iterate over 
the iterable and apply that filter to each of its elements. Finally, it returns the filtered iterable. 
'''
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print("Before filtering my numbers were:\n",numbers)
print("After filtering my numbers are:\n",list(filter(lambda x: x%2==0,numbers)))


'''
3. The map function:

The map function takes a function and an iterable, e.g. list, to iterate over the iterable
and apply that function to each of its elements. Essentially, map carries out a 
transformation. Finally, it returns the modified/transformed iterable. 
'''

org_prices = [20, 30, 50, 80, 300, 500]
print("The prices before discount:\n", org_prices)

discount = 10 #int(input("How much discount do you want to apply?\n"))
disc_prices = list(map( lambda x: x- x*discount/100, org_prices))
print('The prices after a discount of {d}% :\n'.format(d=discount),disc_prices)

'''
4. Combining filter and map:
'''
print("Before filtering for even numbers:\n",numbers)
evens = list(filter(lambda x: x%2==0,numbers))
print("After filtering for even numbers:\n",evens)
evens_squared = list(map(lambda x: x*x, evens))
print("After filtering for even numbers and squaring each:\n",evens_squared)

'''
5. Scope in Python:

- The LEGB Rule defines the visibility of in-built types and of variables defined in three different 
parts (called scopes) of a python code file namely in the Local, Enclosing and Global scopes, as follows:

Local scope: Variables defined (locally) within a function. Will only be used/changed when the function is running.
we can have one global variable and one local variable which have the same name and yet the global one will not be
changed during the function's execution, but only the local one. One can use the global variable by adding a 
"global var_name" in the local scope of the function.

Enclosing scope: Variables defined (locally) within a nesting scope of a function. Similarly to the local scope rule,
variables defined in that scope are the first to be used/changed, but if the variable is not defined there, 
the compiler will look in the closest available scope, here the scope of outer function, and will continue to
do so until it finds the variable. Essentially, variables are available from outer to inner scopes but not the
other way around. One can use the outer scope variable by adding a "non_local var_name" in the scope of the inner 
function.

Global scope: Variables defined in the first indentation of the file. Can be used freely anywhere within the 
file they are defined in, unless overidden in local/enclosing scope and in that case the use of the "global" 
keyword is required in order to use them.

Built-in types: The language's keywords can be used anywhere and do not need to be declared or defined, 
for example: False, True, print, def, class, etc.
'''

