def powerdigitSum(base,exponent):
    digit = [int(a) for a in str(base**exponent)]
    print(sum(digit))

powerdigitSum(2,1000)


