l, r = map(int, input().split())


def func(x):
    x_str = str(x)
    digits = len(x_str)
    first_digit = int(x_str[0])

    sum = 0
    for i in range(1, first_digit):
        sum += i ** (digits - 1)

    for i in range(2, digits):
        for j in range(1, 10):
            sum += j ** (i - 1)

    for i in range(1, digits):
        sum += (min(int(x_str[i]), first_digit) - 1) * (first_digit ** (digits - i - 1))

    return sum


print(func(r) - func(l))
