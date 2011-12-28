"""
/*
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
*/
"""
import math as m

def fsum(n):
    return sum([m.factorial(int(str(n)[i])) for i in range(len(str(n))) ])

print sum([i for i in range(3, 1000000) if i == fsum(i)])
   
