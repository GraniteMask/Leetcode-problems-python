## Brute 1 - Inefficient (limited test cases / not for large inputs)
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