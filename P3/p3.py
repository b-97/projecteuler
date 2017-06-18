from math import sqrt

def is_prime(a):
    if a < 2: return False
    
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True

def max_prime_factor(n):
    primefactors = []
    for i in range(2, int(n/2)):
        if(n < 2): break
        if(n % i == 0):
            if(is_prime(i)):
                primefactors.append(i)
                n /= i
    return max(primefactors)
