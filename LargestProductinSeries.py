#Receive the seires of number and the adjacent digits as input
def seriesproductmax(series, digit):
    #Convert the input into string to iterate through
    series = str(series)
    #Initialize the greatest product value
    product_max = 0

    #Nested loops to iterate through Series until given adjacent digits length
    for i in range(0, len(series) - digit+1):
        product_base = 1
        for j in range(i, i+digit):

            #Compute the product of the values of adjacent digits
            product_base *= int(series[j: j+1])

        #Check if the computed value can be the greatest product value
        if product_max < product_base:
            product_max = product_base

    #Return the greatest product value
    return product_max
