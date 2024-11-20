# 1 

def arrayCheck(list) :
     return any(list[idx: idx + len([1,2,3])] == [1,2,3]
          for idx in range(len(list) - len([1,2,3]) + 1))

print("is [1, 2, 3] in [1, 1, 2, 3, 1]?")
print(arrayCheck([1, 1, 2, 3, 1]))
print("is [1, 2, 3] in [1, 1, 2, 4, 1]?")
print(arrayCheck([1, 1, 2, 4, 1]))
print("is [1, 2, 3] in [1, 1, 2, 1, 2, 3]?")
print(arrayCheck([1, 1, 2, 1, 2, 3]))


# 2
def stringBits(str) :
    newStr = ""
    for index, char in enumerate(str):
        if index % 2 == 0:
             newStr = newStr + char
    return newStr

print("Print every other letter of Hello:")
print(stringBits("Hello"))
print("Print every other letter of Hi:")
print(stringBits("Hi"))
print("Print every other letter of Heeololeo:")
print(stringBits("Heeololeo"))

# 3

def doubleChar(str) :
    newStr = ""
    for index, char in enumerate(str):
        newStr = newStr + 2*char
    return newStr

print("Print twice every letter of The:")
print(doubleChar("The"))
print("Print twice every letter of AAbb:")
print(doubleChar("AAbb"))
print("Print twice every letter of Hi-There:")
print(doubleChar("Hi-There"))

# 4
def count_evens(list) :
    count = 0 
    for item in list:
        if item % 2 == 0:
             count = count + 1
    return count

print("Count number of evens in: [2, 1, 2, 3, 4]")
print(count_evens([2, 1, 2, 3, 4]))
print("Count number of evens in: [2, 2, 0]")
print(count_evens([2, 2, 0]))
print("Count number of evens in: [1, 3, 5]")
print(count_evens([1, 3, 5]))


