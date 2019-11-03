#! python


def sum_digits(exp):
    x = str(2**exp)
    print(x)
    y = list(x)
    z = 0
    for ind in range(len(y)):
        z += int(y[ind])
    print(z)


sum_digits(15)
sum_digits(1000)
sum_digits(2000)
sum_digits(10000)

# Lol
