import math
#My Naive Approach
def LargestPF(n):
    Factors = []
    PrimeFactors = []
    for i in range(1, n+1):
        if n % i == 0:
            Factors.append(i)
    for x in Factors:
        if (x%3 == 0) or (x%5 == 0) or (x%7 == 0) or (x%11 == 0):
            PrimeFactors.append(x)

    return max(PrimeFactors)

#Solution
def LargestPF1(n):
    #Check if the number is even
    while n % 2 == 0:
        max_prime = 2
        n /= 1
    #Assuming number is odd, run Sieve of Eratosthenes
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n = n/i

    if n > 2:
        max_prime = n
    return int(max_prime)




print(LargestPF1(600851475143))