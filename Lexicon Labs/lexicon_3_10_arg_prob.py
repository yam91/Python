'''
def func(a,b, *args) :
    print(a,b)
    print(args)

func(1,2,3,4,5)
'''

def func1(a, b, name = 'John', *args, **kwargs) :
    print(a)
    print(b)
    print(args)
    print(name)
    print(kwargs)

func1(1, 2, name='Anna', 3, age=34)