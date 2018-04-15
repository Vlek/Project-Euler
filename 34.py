result = 0

factorialsDict = {0: 1, 1: 1, 2: 2}

def factorial( number ):
    step = number
    if number not in factorialsDict:
        result = 1
        while step > 1:
            result *= step
            step -= 1
        factorialsDict[number] = result
    return factorialsDict[number]

def isEqualToFactorSum( number ):
    result = 0
    for i in str(number):
        result += factorial( int(i) )
    return result == number




if __name__ == "__main__":
    assert( isEqualToFactorSum( 145 ) )
        
    factors = []
    for number in range(3, 100000):
        if isEqualToFactorSum(number):
            result += number
            factors.append(number)

    print('The total amount is {}'.format(result))
    print factors
