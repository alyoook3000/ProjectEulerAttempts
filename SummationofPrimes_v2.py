#Approach 1
def primeSum_naive(limit):
    primes = []
    for x in range(1, limit+1):
        if (x>1):
            for i in range(2,x):
                if(x%i)==0:
                    break
                else:
                    primes.append(x)

    return sum(primes)


#Approach 2
import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(n):
    sum = 0
    for i in range(1, n):
        if is_prime(i):
            sum += i
    return sum

def main():
    print(sum_primes(2000000))