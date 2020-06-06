#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sqsum(to):
    return sum(i ** 2 for i in range(1, to))


def sumsq(to):
    return sum(i for i in range(1, to)) ** 2


print(sumsq(101) - sqsum(101))


#Output: 25164150
