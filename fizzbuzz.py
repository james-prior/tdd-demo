def fizzbuzz(x):
    if is_multiple_of_three(x) and is_multiple_of_five(x):
        return 'fizzbuzz'
    if is_multiple_of_three(x):
        return 'fizz'
    if is_multiple_of_five(x):
        return 'buzz'
    return x

def is_multiple_of_three(x):
    return x % 3 == 0

def is_multiple_of_five(x):
    return x % 5 == 0
