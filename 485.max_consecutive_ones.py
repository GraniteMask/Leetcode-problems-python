class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        l = 0
        final = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                l += 1
                final = max(final, l)
            else:
                l = 0
                final = max(final, l)
                
        return final