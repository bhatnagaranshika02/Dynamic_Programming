class Knapsack:
    def __init__ (self,numofitems,capacity,weight,profit):
        self.numofitems = numofitems
        self.capacity=capacity
        self.weight=weight
        self.profit=profit
        self.dptable = [[0 for x in range(capacity+1) ] for x in range(numofitems+1)]
    def dynamicProgramming(self):
        
        for i in range(1,self.numofitems+1):
            for j in range(1,self.capacity+1):
                notTaking = self.dptable[i-1][j]
                takingItem=0

                if self.weight[i]<=j:
                    takingItem = self.profit[i]+self.dptable[i-1][j-self.weight[i]]
                self.dptable[i][j] = max(notTaking,takingItem)



    def show(self):
        print("Total benefit: ",self.dptable[self.numofitems][self.capacity])
        j=self.capacity
        for n in range(self.numofitems,0,-1):
            if self.dptable[n][j]!=0 and self.dptable[n]:
                print("We take item",n)
                j=j-self.weight[n]

numofitems = 4
capacity = 7
weight = [0,1,3,4,5]
profit = [0,1,4,5,7]

k=Knapsack(numofitems , capacity , weight , profit)
k.dynamicProgramming()
k.show()
