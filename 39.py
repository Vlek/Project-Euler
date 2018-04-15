"""
Answer: 840
"""

def isRightTriangle( a, b, c ):
    return a ** 2 + b ** 2 == c ** 2

def getPerimeter( a, b, c ):
    return a + b + c


if __name__ == "__main__":

    rightTriangles = {}
    for a in range( 1, 401 ):
        for b in range( 1, 401 ):
            for c in range( 1, 401 ):
                if isRightTriangle( a, b, c ):
                    if getPerimeter(a, b, c) in rightTriangles:
                        if [a, b, c] not in rightTriangles[ getPerimeter( a, b, c) ]:
                            rightTriangles[ getPerimeter( a, b, c) ].append( [a, b, c] )
                    else:
                        rightTriangles[ getPerimeter( a, b, c) ] = [[a, b, c]]

    result = 0
    for i in rightTriangles:
        if len( rightTriangles[ i ] ) > result:
            result = len( rightTriangles[ i ] )
            answer = i

    print 'The perimeter with the most solutions is: {}'.format( answer )
