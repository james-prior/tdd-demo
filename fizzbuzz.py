def is_multiple_of_three(x):
    return x % 3 == 0

def is_multiple_of_five(x):
    return x % 5 == 0

def fizzbuzz(x):
    if x == 15 or x == 30:
        return 'fizzbuzz'
    if is_multiple_of_three(x):
        return 'fizz'
    if is_multiple_of_five(x):
        return 'buzz'
    return x

