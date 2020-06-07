#Find the sum of all the primes below two million.
def isPrime(n):
    if n < 2: return "Neither prime, nor composite"

    for i in range(3, int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True


def sumofprime(upto):
    sum=2
    for i in range(7,upto+1,2):
        if isPrime(i):
            sum+=i
    return sum

print(sumofprime(2000000))


#Output: 142913828922
