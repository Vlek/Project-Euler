"""
answer: 748317
"""


def primesToNumber(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def mince( number ):
    minceable = str( number )
    return [minceable[i:] for i in range(len(minceable))] + [minceable[:-i] for i in range(1, len(minceable))]

def allPrime( numberList ):
    for number in numberList:
        if int( number ) not in primes:
            return False
    return True

if __name__ == "__main__":
    assert( mince( 3797 ) == ['3797', '797', '97', '7', '379', '37', '3'] )

    primes = primesToNumber( 1000000 )
    result = []
    
    for prime in primes:
        if allPrime( mince( prime ) ):
            result.append( prime )


    print( 'The list of trunable primes is {} long, and contains: {}'.format( len( result ), result))
