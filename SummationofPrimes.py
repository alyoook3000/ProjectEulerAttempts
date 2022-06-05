def prime_sum_sieve(limit):
    nums = [i for i in range(1, limit+1)]
    is_prime = [True for i in nums]
    is_prime[0] = False
    list_prime = []
    sumPrimes = sum(list_prime)


    nums = [i for i in range(1, limit+1)]
    prime_array = [True for i in nums]

    for num in nums:
        if is_prime[num-1] == False:
            continue
        else:
            for i in range(num*2, limit+1, num):
                is_prime[i-1] = False

    for i in range(2, len(prime_array)):
        if is_prime[i] == True:
            list_prime.append(nums[i])

    return sumPrimes

