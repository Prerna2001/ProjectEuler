#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sqsum(to):
    if to==0:
        return 0
    else:
        return to*(to+1)*(2*to+1)/6

def sumsq(to):
    if to==0:
        return 0
    else:
        return (to*(to+1)/2)**2


print(sumsq(100)-sqsum(100))

#Output: 25164150
