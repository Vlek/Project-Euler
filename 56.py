


if __name__ == "__main__":
    result = 0
    for a in range(1,101):
        for b in range(1,101):
            currentTest = a ** b
            digitSum = sum([ int(i) for i in str(currentTest)])
            if digitSum > result:
                result = digitSum

    print result
