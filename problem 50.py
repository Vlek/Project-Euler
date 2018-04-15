"""
answer: 997651
"""

def primesToNumber(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


primeSums = {}

primes = primesToNumber( 1000000 )

intermediary = 0
currentSum = 0

for prime in reversed( primes ):
    for step in range(len(primes)):
        intermediary = step
        while currentSum < prime:
            currentSum += primes[intermediary]
            intermediary += 1
        if currentSum == prime:
            primeSums[prime] = primes[step:intermediary]
            #print "{}: {} ({})".format(prime, primeSums[prime],len(primeSums[prime]))
            break #Smaller numbers are always going to have greater prime sums.
        currentSum = 0
    if len(primeSums) > 1000:
        #We don't need a sum path for every prime, just the thousand largest ones we can find.
        break


result = 0
prime = 1
for i in primeSums:
    if len(primeSums[i]) > result:
        prime = i
        result = len(primeSums[i])


print "The answer is {} with {} consecutive primes making up the prime".format(prime, result)
