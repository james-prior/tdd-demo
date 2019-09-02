def is_multiple_of_three(x):
    return x % 3 == 0

def fizzbuzz(x):
    if is_multiple_of_three(x):
        return 'fizz'
    if x % 5 == 0:
        return 'buzz'
    return x

