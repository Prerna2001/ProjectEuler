#Find the sum of all the primes below two million.
a = 2000000
numbers = set(range(3, a + 1, 2))
for number in range(3, int(a ** 0.5) + 1):
    if number not in numbers:
        continue
        num = number
    while num < a:
        num += number
        if num in numbers:
            numbers.remove(num)

print (2 + sum(numbers))


#Output: 142913828922
