length = 0
result = 1
numbers = []
currentNumber = 1

while length < 1000000:
    for i in str(currentNumber):
        for g in [0,99,999,9999,99999,999999]:
            if length == g:
                numbers.append( int(i) )

        length += 1
    currentNumber += 1


for i in numbers:
    result *= i
print result
