def ispallindome(n):
    c,t=0,n
    while(t>0):
        c=c*10+t%10
        t//=10

    if c==n:
        return True
    else:
        return False

def greatnum():
    top=0
    for i in range(999,100,-1):
        for j in range(i-1,100,-1):
            if ispallindome(i*j) and i*j>top:
                top = i*j
    return top
print(greatnum())