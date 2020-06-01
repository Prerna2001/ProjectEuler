#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

s1=0
s2=0
for i in range (101):
    s1=s1+i
    s2=s2+(i*i)
s3=(s1*s1)-s2
print(s3)


#Output: 25164150
