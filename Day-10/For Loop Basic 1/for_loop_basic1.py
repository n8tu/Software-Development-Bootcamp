def basic():
    for i in range(1,151,1):
        print(i)

def multiplesOfFive():
    for i in range(5,1001,5):
        print(i)

def countingTheDojoWay():
    for i in range(1,101):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)

def whoaThatSuckersHuge():
    sum = 0
    for i in range(0,500001):
        sum += i
    print(sum)

def countDownByFours():
    for i in range(2018,-1,-4):
        print(i)


def flexibleCounter(lowNum, highNum, mult):
    for i in range(lowNum,highNum+1):
        if i % mult == 0:
            print(i)


