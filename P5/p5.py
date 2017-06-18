def divisiblefrom1to20(n):
    for i in [11,12,13,14,15,16,17,18,19]:
        if(n % i != 0):
            return False
    return True

def smallestmultiple():
    n = 2520
    while not divisiblefrom1to20(n):
        n += 20
    print(n)
    return n
