def summum():
    Multiplessum = []
    for i in range(1000):
        if (i%3) == 0 or (i%5) == 0:
            Multiplessum.append(i)
    Multiplessum = sum(Multiplessum)

    return Multiplessum


