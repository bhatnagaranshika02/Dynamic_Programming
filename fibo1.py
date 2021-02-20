def fib(n):
    dp=[0]*(n+1)
    
    dp[0]=0
    dp[1]=1

    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp

print(fib(19))


def fib2(n,dp):
    if n<=1:
        return n

    elif n>1:
        dp[n]=fib2(n-1,dp)+fib2(n-2,dp)
        return dp[n]

    elif dp[n]!=-1:
        return dp[n]
    else:
        pass

n = int(input())
dp=[0]*(n+1)
print(fib2(n,dp))

      
