#What is the largest prime factor of the number 600851475143 ?

from math import sqrt
def primef():
    arr,c=[],0
    n=600851475143
    t=int(sqrt(n))
    for i in range(2,t):
        if(n%i==0):
            n/=i
            arr.insert(c,i)
            c+=1
    return arr[len(arr)-1]


print(primef())


#Output:6857
