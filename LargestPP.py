def Bigpp():
    pal = []
    for i in range(100, 1000):
        for j in range(i,1000):
            product = str(i*j)
            if product == product[::-1]:
                pal.append(int(product))

    print(max(pal))

Bigpp()