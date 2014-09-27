"""
Primality test
"""
def is_prime(num):
    if num <=3:
        if num <=1:
            return False
        return True
    if not num % 2 or not num % 3:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):
            if not num % i or not num % (i + 2):
                return False
    return True
“””
http://en.wikipedia.org/wiki/Fermat's_factorization_method

I need to come up with a way of representing Fermat’s method in code

“””