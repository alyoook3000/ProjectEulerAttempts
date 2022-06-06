def seriesproductmax(series, digit):
    series = str(series)
    product_max = 0

    for i in range(0, len(series) - digit+1):
        product_base = 1
        for j in range(i, i+digit):
            product_base *= int(series[j: j+1])
        if product_max < product_base:
            product_max = product_base

    return product_max
