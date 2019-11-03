#! python

from functools import reduce

result = 1
x = list(range(1, 21))


def lcm(*values):
    # Read as for each value in values, add value to values
    # List comprehension creates list for function
    values = [value for value in values]
    if values:
        n = max(values)
        m = n
        values.remove(n)
        # While any remainder exists, double amount until 0 is found
        while any(n % value for value in values):
            n += m
        '''Return least common multiple for all iterated #'s
        Since smallest possible # has been tested for in previous
        line n += works'''
        return n
    return 0


for y in x:
    # line below feeds tuple to function
    # result == to lcm, y is current # from 1-20
    result = lcm(result, y)
print(result)

print(reduce(lcm, range(1, 21)))
