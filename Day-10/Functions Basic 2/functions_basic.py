def countDown(number):
    list = []
    for i in range(number,-1,-1):
        list.append(i)
    return list

def printAndReturn(numbers):
    print(numbers[0])
    return numbers[1]

def firstPlusLength(numbers):
    return numbers[0] + len(numbers)

def valuesGreaterThanSecond(numbers):
    list = []
    if(len(numbers) < 2):
        return False
    else:
        for i in range(0,len(numbers)):
            if(i > numbers[1]):
                list.append(i)
            else:
                continue;
    
    print(len(list))
    return list

def thisLengthThatValue(size, value):
    list = []
    for i in range(0,size):
        list.append(value)
    
    return list

