#Problem 48

def selfpower(to):
    '''adds all of the self powers together up to to'''
    return sum([ num**num for num in range(1, to + 1) ])



if __name__ == '__main__':
    print(str(selfpower(1000))[-10:])
