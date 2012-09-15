
def isPrime(n):
    import re
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None
    
    
def genPrimes(n):
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n/3)
    
    for i in xrange(1, int(n**0.5)/3 + 1):
      if sieve[i]:
        k = 3*i+1|1
        sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
        
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]


def primeFactors(n):
    factors = []
    lastresult = n

    if n == 1:
        return [1]

    while 1:
        if lastresult == 1:
            break
        c = 2
        while 1:
            if lastresult % c == 0:
                break
            c += 1
        factors.append(c)
        lastresult /= c

    return factors

