def biggieSize(numbers):
    for i in range(0,len(numbers)):
        if numbers[i] > -1:
            numbers[i] = "big"
    return numbers

def countPositives(list):
    count = 0
    for i in list:
        if i > 0:
            count += 1
        else:
            continue
    
    list[len(list)-1] = count
    return list

def sumTotal(list):
    sum = 0
    for i in list:
        sum += i
    return sum

def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)


def length(list):
    return len(list)

def minimum(list):
    if len(list) == 0:
        return False
    else:
        small = list[0]
        for i in list:
            if i < small:
                small = i
        return small

def maximum(list):
    if len(list) == 0:
        return False
    else:
        small = list[0]
        for i in list:
            if i > small:
                small = i
        return small


def ultimateAnalysis(list):
    dict = {
        'sumTotal':sumTotal(list),
        'average':average(list),
        'minimum':minimum(list),
        'maximum':maximum(list),
        'length':length(list)
        }
    return dict

def reverseList(list):
    list = list[::-1]
    return list





