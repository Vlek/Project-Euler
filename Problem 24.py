#Problem 24

import itertools

if __name__ == "__main__":
    digits = ['0','1','2','3','4','5','6','7','8','9']
    perms = itertools.permutations( ''.join(digits) )
    result = [i for i in perms]
    perms.sort()
    print('The answer is: {}'.format( permutations[999999] ) )
