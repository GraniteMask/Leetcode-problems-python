# Brute - Limited test case solution

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        length = len(nums)
        count = 0 
        
        for j in range(length - 1,-1,-1):
            
            if j == 0:
                break
            else:
                temp = 2*nums[j]
                # print(temp)
                for i in range(j-1,-1,-1):
                    
                    if nums[i] > temp:
                        # print("nums", i)
                        count += 1
        
                        
        return count
                