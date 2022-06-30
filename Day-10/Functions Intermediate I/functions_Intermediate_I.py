import random
def randInt(min = 'random', max = 'random'):
    if min == 'random' and max == 'random':
        return round(random.random() * 100)
    elif min != 'random' and max == 'random':
        return round(random.random() * (100-min) + min)
    elif max != 'random' and min == 'random':
        return round(random.random() * max)
    else:
        return round(random.random() * (max-min) + min)

#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500


