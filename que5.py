#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


listuse = [11, 13, 14, 15, 16, 17, 18, 19]
prime = [2, 3, 5, 7, 11, 13, 17, 19]
def isdivisible(num):
    for i in listuse:
        if num % i !=0:
            return False
    return True

min = 1
for i in prime:
    min *= i
test = min

while True:
    if isdivisible(min):
        print(min)
        break
    min+=test
        
        
  #output: found an answer: 232792560
