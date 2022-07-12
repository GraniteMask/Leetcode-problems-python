class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        t = [[0]*(amount+1) for i in range(len(coins)+1)]
        
        if len(coins) == 1:
            if amount % coins[0] == 0:
                return amount//coins[0]
            elif amount == 0:
                return 0
            else:
                return -1
        
        
        for i in range(len(coins)+1):
            for j in range(amount+1):
                if i == 0:
                    t[i][j] = sys.maxsize - 1
                if j == 0:
                    t[i][j] = 0
              
        
                    
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                
                if coins[i-1] <= j:
                    t[i][j] = min(1 + t[i][j-coins[i-1]], t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
                    
        print(sys.maxsize - 1)
        
        if t[-1][-1] == sys.maxsize - 1:
            return -1
        else:
            return t[-1][-1]