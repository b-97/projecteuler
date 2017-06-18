def sumofsquares(n):
    summation = 0
    for i in range(0, n + 1):
        summation += i ** 2
    return summation

def squareofsum(n):
    summation = 0
    for i in range(0, n+1):
        summation += i
    return summation ** 2

