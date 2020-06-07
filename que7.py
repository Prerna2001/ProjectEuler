#What is the 10001st prime number?

def isPrime(n):
    if n < 2: return "Neither prime, nor composite"
    for i in range(3, int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True


def nthPrime(n):
    numberOfPrimes = 1  # 2 is not in prime ( 1 st no. prime is 3

    prime = 1

    while numberOfPrimes < n:
        prime += 2
        if isPrime(prime):
            numberOfPrimes += 1

    return prime

print(nthPrime(10001))


#Output:104743
