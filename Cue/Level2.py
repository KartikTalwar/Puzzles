
#  Write code to find the first prime fibonacci number larger than a given minimum
#  Step 1. Use your code to compute the smallest prime fibonacci number
#          greater than 227,000.  Call this number X.
#  Step 2. The password for level 3 is the sum of prime divisors of X + 1.

def fibonacci(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fibonacci(n/2)
        c    = a*(2*b - a)
        d    = b*b + a*a
        return (c, d) if n%2 == 0 else (d, c+d)


def generatePrimes(n):
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n/3)
    
    for i in xrange(1, int(n**0.5)/3 + 1):
      if sieve[i]:
        k = 3*i+1|1
        sieve[k*k/3::2*k]             = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
        
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]


def nthPrimeFibonacci(n):
    primes = generatePrimes(n*10)

    for i in range(n*5):
        fib = fibonacci(i)[0]
        if fib > n and fib in primes:
            return fib


def primeFactors(x):
    factors = []
    i = 2

    while i <= x:
        if x % i == 0:
            x /= i
            factors.append(i)
        else:
            i += 1

    return set(factors)


print sum(primeFactors(nthPrimeFibonacci(227000)+1))

