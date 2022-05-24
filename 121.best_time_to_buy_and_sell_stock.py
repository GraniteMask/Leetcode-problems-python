## Brute - Inefficient (limited test cases / not for large inputs)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = []
        
        if len(prices) >=1 and len(prices) <=100000:
            for i in range(len(prices)-1):
                if prices[i] >= 0 and prices[i] <= 10000:
                    maxtemp = 0
                    for j in range(i+1, len(prices)):
                        if prices[j] >= 0 and prices[j] <= 10000:
                            diff = prices[i]-prices[j]
                            print(diff)
                            if abs(diff) > maxtemp and diff < 0:
                                maxtemp = abs(diff) 
                    maxProfit.append(maxtemp)
                    print("maxtemp", maxtemp)

        if len(maxProfit) == 0:
            return 0
        else:
            return max(maxProfit)


## Optimized solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit=0
        
        for i in range(len(prices)-1):
            if prices[l] > prices[r]:
                l=r
            elif prices[r] > prices[l]:
                if maxProfit == 0:
                    maxProfit = prices[r] - prices[l]
                else:
                    temp = prices[r] - prices[l]
                    if temp > maxProfit:
                        maxProfit = temp
                        
            r=r+1
            
        return maxProfit
            