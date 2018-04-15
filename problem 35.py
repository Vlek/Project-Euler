def primesToNumber(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def rotateList( thing ):
    result = [thing]
    thing = str( thing )
    for i in range( len( thing ) - 1 ):
        thing = thing[1:] + thing[:1]
        result.append( int( thing ) )
    return result

def allPrime( numberList ):
    for i in numberList:
        if i not in primesList:
            return False
    return True

if __name__ == "__main__":
    result = {}
    primesList = primesToNumber( 1000000 - 1 )

    for number in range( 1, 1000000 ):
        if number not in result:
            
            rotations = rotateList( number )
            
            if allPrime( rotations ):
                for i in rotations:
                    result[ i ] = ''

    print 'There are {} circular primes under one million'.format( len( result ) )
