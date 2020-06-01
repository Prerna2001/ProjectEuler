#What is the sum of the digits of the number 21000?
p=pow(2,1000)
p=str(p)
sum=0
for i in p:
    sum=sum+int(i)
print(sum)

#Output:1366
