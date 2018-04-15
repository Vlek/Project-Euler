"""
answer: 5482660
"""


def pentagonalNumbersTo( number ):
    return [ (i * (3 * i - 1) / 2 ) for i in range(1, number + 1) ]


if __name__ == "__main__":

    pentNumbers = pentagonalNumbersTo(10000)

    result = 10000000
    
    for j in pentNumbers:
        for k in pentNumbers[:int( len(pentNumbers) * .75 ) ]: #I want 75% of it because most of the upper additions aren't going to be in there.
            if (j + k) in pentNumbers and abs( j - k ) in pentNumbers and abs( j - k ) < result:
                print j, k, abs( j-k )
                result = abs(j - k)

    print 'The minimalized difference between a pentagonal pair is {}'.format(result)
