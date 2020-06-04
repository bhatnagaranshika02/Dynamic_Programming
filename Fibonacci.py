class fibo:
    def __init__ (self):
        self.memoi = {}
        self.memoi[0] = 0
        self.memoi[1]=1

    def fibMemoi(self,n):
        if n in self.memoi:
            return self.memoi[n]

        self.memoi[n-1] = self.fibMemoi(n-1)
        self.memoi[n-1] = self.fibMemoi(n-1)

        c = self.memoi[n-1]+self.memoi[n-2]
        self.memoi[n] = c

        return c

    def naive(self,n):
        if n==1:
            return 0
        if n==1:
            return 1
        return self.naive(n-1)+self.naive(n-2)


if __name__ == "__main__":
    fib = fibo()
    print(fib.fibMemoi(6))
    print(fib.fibMemoi(6))
