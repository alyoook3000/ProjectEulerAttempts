def diff(n):
    sum = 0
    square = 0
    for i in range(n+1):
        sum += i**2
        square += i
    square = square**2
    diff = square - sum

    return diff
