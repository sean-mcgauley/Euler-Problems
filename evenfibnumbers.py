#! python

# a is trailing number, b is previous number + current number
a, b = 1, 1
# total of numbers
total = 0
# leading number, while less than 4000000
while a <= 4000000:
    if a % 2 == 0:
        # add leading number to total
        total += a
    a, b = b, (a + b)
    # on 1st >>> 1, 2
    # on 2nd >>> 2, 3
    # on 3rd >>> 3, 5
    # on 4th >>> 5, 8

print(total)
