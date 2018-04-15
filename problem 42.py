k = open('words.txt', 'r')

words = k.readlines()[0]
words = words.split('''","''')

longestWord = 0
for i in words:
    if len(i) > longestWord:
        longestWord = len(i)

print( 'The longest word was {} characters long.'.format(longestWord) )
print( 'Creating triangle number list up to {}.'.format( longestWord * 26 ) )

def triangles2Number( number ):
    result = [1]
    step = 2
    while result[-1] < number:
        result.append( 0.5 * step * (step + 1) )
        step += 1
    return result

trianglesList = triangles2Number( longestWord * 26 )

letterNums = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,'"':0}
triangleWords = 0
for i in words:
    if sum( [letterNums[letter.lower()] for letter in i] ) in trianglesList:
        triangleWords += 1

print('There were {} triangle words'.format(triangleWords))
