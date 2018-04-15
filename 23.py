"""
Incorrect answers:

391257632

"""

def isAbundant( number ):
    divisors = 0
    for i in range(1,  number / 2 + 1 ):
        if number % i == 0:
            divisors += i
    return divisors > number

abundantNumbers = []
for i in range(28124):
    if isAbundant( i ):
        abundantNumbers.append(i)

def isAbundantSum( number ):
    for i in abundantNumbers:
        if i > number:
            return False
        if ( number - i ) in abundantNumbers:
            return True

if __name__ == "__main__":
    assert( isAbundant( 12 ) )
    assert( isAbundantSum( 24 ) )

    result = 0
    for number in range( 28123 ):
        if not isAbundantSum( number ):
            result += number

    print 'The total of all numbers that are not the sum of two abundant numbers is {}'.format( result )
