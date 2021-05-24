import math

def getMedian(data):
    median = 0
    for x in data:
        median += x

    print("\nMedian")
    median = median / len(data)
    print (median)
    return median


def standardDeviation(data):
    newlist = []
    squareArray  = []
    result = 0
    
    medianValue = getMedian(data)

    for x in data:
        value = x - medianValue;         #23 - 15 = 8
        newlist.append(abs(value))       #abs is use for positive number only

    print("\nStandat Diviation Array")
    for y in newlist:
        print(y);
        squareArray.append(math.pow(y,2))

    for z in squareArray:
        result += z

    result = result / len(squareArray)

    print("Variance:")
    print(result) 
    print("Standar Diviation:")
    result = math.sqrt(result)
    print(result)

data = [15,16,18,19,22,24,29,30,34]
standardDeviation(data)


###
#Same function as in stadistics but now imported from numpy

import numpy as np

data = [15,16,18,19,22,24,29,30,34]

print("STD:", np.std(data))
print("Median:", np.median(data))
print("25th Percentile:", np.percentile(data, 25))

###