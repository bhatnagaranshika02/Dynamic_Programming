import sys
sys.setrecursionlimit(10**6)

def fib(n):
    f=[0 for i in range(n+1)]
    f[0]=0
    f[1]=1
    for i in range(2,n+1):
        f[i]=f[i-1]+f[i-2]
    print(*f)




def fib_rec(n):
    if n<=1:
        return n
    return fib_rec(n-1)+fib_rec(n-2)



def fact(n):
    f=[0 for i in range(n+1)]
    f[1]=1
    f[2]=2
    for i in range(3,n+1):
        f[i]=i*f[i-1]
    print(*f)

fact(6)


