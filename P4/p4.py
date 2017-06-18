def testpalindrome(n):
    digits = []
    while(n > 0):
        digits.append(n % 10)
        n = n // 10
    print(digits)
    for i in range(0, len(digits)):
        if(digits[i] != digits[(len(digits) - 1) - i]):
            return False
    return True

def largestpalindromeproduct():
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if testpalindrome(i * j):
                palindromes.append(i * j)
    return max(palindromes)
