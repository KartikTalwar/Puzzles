"""
/*
    The Fibonacci sequence is defined by the recurrence relation:

    F_n = F_n1 + F_n2, where F_1 = 1 and F_2 = 1.
    Hence the first 12 terms will be:

    F_1 = 1
    F_2 = 1
    F_3 = 2
    F_4 = 3
    F_5 = 5
    F_6 = 8
    F_7 = 13
    F_8 = 21
    F_9 = 34
    F_10 = 55
    F_11 = 89
    F_12 = 144
    The 12th term, F_12, is the first term to contain three digits.

    What is the first term in the Fibonacci sequence to contain 1000 digits?
*/



Fib(n) = ( (1+sqrt5)/2 )^n / sqrt5
Len(n) = floor(log10(n) + 1 )

Len(Fib(n)) = log10( ( (1+sqrt5)/2 )^n / sqrt5 ) + 1
Len(Fib(n)) = log10( ( (1+sqrt5)/2 )^n ) - log10( sqrt5 ) + 1
Len(Fib(n)) = nlog10( (1+sqrt5)/2 ) - 0.5log10(5) + 1

nlog10( (1+sqrt5/2) ) = Len(Fib(n)) + 0.5log10(5) -1
n = ( Len(Fib(n)) + 0.5log10(5) -1 )/ ( log10( (1+sqrt5)/2 ) )

"""

import math as m

print int(m.ceil( (1000 + m.log10(5)/2 -1) / ( m.log10((1+m.sqrt(5))/2) ) ))

