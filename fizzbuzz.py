
def fizzbuzz(n):
    output = ''
    if n % 3 == 0:
        output += 'fizz'
    if n % 5 == 0:
        output += 'buzz'
    return output or str(n)
