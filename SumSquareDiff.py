#! python

x = [i for i in range(1, 101)]
n = 0
z = 0

for i in x:
    n += i**2
    z += i

z **= 2

h = z - n

print(h)

# Alternative list comprehension solution

sequence = range(1, 101)
sum_of_squares = sum([i**2 for i in sequence])
square_of_sum = sum(sequence)**2
print(square_of_sum - sum_of_squares)
