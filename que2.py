
def fibonacci():
    a,b,i=1,2,2
    fibo = [a,b]
    sum=b
    while(b<4000000):
       c=a+b
       a,b=b,c
       fibo.insert(i,b)
       i+=1
    return fibo
def sumevenfibo():
    sum=0
    arr=fibonacci()
    x= len(arr)-1
    for i in range(1,x):
            sum+=arr[i]
            i=i+1
    return sum
print(sumevenfibo())
