def largest_factor(x):
    divisor = 2
    while x > 1:
        quotient, remainder = divmod(x, divisor)
        if remainder == 0:
            x = quotient
        else:
            divisor += 1
    return divisor
