from math import sqrt
from itertools import count, islice


class PrimeCheck(object):
    def __init__(self):
        pass

    @staticmethod
    def is_prime(num):
        return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num)-1)))

    @staticmethod
    def is_prime_v2(x):
        if x < 2:
            return False
        for n in range(2, (x-1)):
            if x % n == 0:
                return False
        else:
            return True


def divisors(n):
    return len([1, n]) if PrimeCheck.is_prime(n) else len([x for x in range(1, n+1) if n % x == 0])