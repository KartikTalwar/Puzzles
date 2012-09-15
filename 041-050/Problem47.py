"""

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct primes factors. 
What is the first of these numbers?

"""

import itertools

def distinct(n):
    return len(set(prime_factors(n)))

n = 0
for i in itertools.count(10000):
    pf = distinct(i)

    if pf == 4:
        n += 1
        if n == 4:
            print i - 3
            break
    else:
        n = 0

