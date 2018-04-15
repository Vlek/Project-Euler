


if __name__ == "__main__":
    result = 0

    for i in range( 10000 ):
        for w in range(1, 10):
            if len( str( w ** i ) ) == i:
                result += 1

    print( result )
