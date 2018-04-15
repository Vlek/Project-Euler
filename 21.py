#Problem 21 by Vlek

def d( number ):
    '''Gets all proper divisors of number'''
    return sum( [1] + [ i for i in range(2, number / 2 + 1) if number % i == 0 ] )

assert(d(220) == 284)
assert(d(284) == 220)


result = 0

numbers = [i for i in range(2, 10001)]

while numbers != []:
    possiblepair = d(numbers[0])
    if possiblepair <= 10000 and possiblepair != numbers[0] and d(possiblepair) == numbers[0]:
      result += possiblepair + numbers[0]
      numbers.pop(numbers.index(possiblepair))
    numbers.pop(0)

print result
