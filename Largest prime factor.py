#! python

x = 600851475143
# look for prime factors

'''Division method, divide number by smallest prime
   Take new number and find smallest prime, repeat
   until quotient is 1, this will be largest prime'''


def largest_prime_factor(n):
    i = 2
    factors = []
    '''A number's largest prime factor will always be
       smaller than the square root of n'''
    while i * i <= n:
        if n % i:    # if this produces a 0 then else statement triggers
            i += 1
        else:
            n //= i  # produces integer, /= floating point
            factors.append(i)
    if n > 1:
        factors.append(n)
    return n, factors


print(largest_prime_factor(x))
