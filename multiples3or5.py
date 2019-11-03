#! python

total_sum = 0

for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        total_sum += x

print(total_sum)

# Algorthimic approach
i = 3 * (999 // 3) * ((999 // 3) + 1) / 2
z = 5 * (999 // 5) * ((999 // 5) + 1) / 2
h = 15 * (999 // 15) * ((999 // 15) + 1) / 2

A = i + z - h

print(A)
