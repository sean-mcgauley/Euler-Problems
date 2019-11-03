#! python

import math


def find_prime(primecount):
    count = 0
    x = 2
    while count < primecount:
        for i in range(2, x + 1):
            if x == i:
                count += 1
            if (x % i) == 0:
                break
        x += 1
    return x - 1

# Solution above takes upwards of a minute
# Solution below takes ~1s


def primes_sieve(n):
    p_n = int(2 * n * math.log(n))  # Overestimate number of primes
    sieve = [True] * p_n  # Everything is prime to start
    count = 0
    for i in range(2, p_n):
        if sieve[i]:  # If number in list is still prime then continue
            count += 1  # count the prime
            if count == n:  # if count is equal to number of primes then end
                return i
            for j in range(2*i, p_n, i):  # eliminated multiples of i
                sieve[j] = False


print(primes_sieve(10001))
