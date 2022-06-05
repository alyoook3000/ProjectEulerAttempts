import math
def tripletproduct(sidesum):

#Euclid's formula:

#a = m**2 - n**2
#b = 2mn
#c = m**2 + n**2
#m > n > 0

#Derived formula
#a+b+c = 2m**2 + 2mn = 2m(m+n)

#2 * m * (m+n) = sidesum
#n = (sidesum / (2*m))-m
    #For loop range set to sqrt of sidesum becuase that is the max integer the result can become
    for m in range(1, round(math.sqrt(sidesum))):
        n = (sidesum / (2*m))-m
        # m have to be larger than n
        if n < 0 or n>= m:
            continue
        if 2 * m * (m+round(n)) == sidesum:
            return (m**2-n**2, 2*m*n, m**2 + n**2)



a, b, c = tripletproduct(1000)
