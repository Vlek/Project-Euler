step = 124000
numResults = 0
while True:
    results = [ ( list( str( step * d ) ) ) for d in range( 1, 7 ) ]
    unsorted = list(results)
    [ x.sort() for x in results ]
    sameDigits = []
    if sum([ len(d) for d in results ]) == len(results[0]) * len( results ) and results.count(results[0]) == 6:
        print results
        print step
        print [ step * d for d in range(1,7) ]
        break
    step += 1
