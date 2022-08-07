# BRUTE FORCE

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if i != j:
                    temp *= nums[j]
            res.append(temp)
            
        return res

# OPTIMIZED and O(1) extra space complexity solution

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1]*(len(nums))
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res