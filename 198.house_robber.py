class Solution:
    def rob(self, nums: List[int]) -> int:
        
        t = [-1]*(len(nums)+1)
        
        def recursion(idx, nums):
            if idx == 0:
                return nums[idx]
            if idx < 0:
                return 0
            
            if t[idx] != -1:
                return t[idx]
            
            pick = nums[idx] + recursion(idx - 2, nums)
            notPick = recursion(idx - 1, nums)
            
            t[idx] = max(pick, notPick)
            return t[idx]
        
        return recursion(len(nums)-1, nums)