class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        t1 = [-1]*(len(nums[1:])+1)
        t2 = [-1]*(len(nums[:-1])+1)
        
        def recursion1(idx, nums):
            if idx == 0:
                return nums[idx]
            if idx < 0:
                return 0
            
            if t1[idx] != -1:
                return t1[idx]
            
            pick = nums[idx] + recursion1(idx - 2, nums)
            notPick = recursion1(idx - 1, nums)
            
            t1[idx] = max(pick, notPick)
            return t1[idx]
        
        def recursion2(idx, nums):
            if idx == 0:
                return nums[idx]
            if idx < 0:
                return 0
            
            if t2[idx] != -1:
                return t2[idx]
            
            pick = nums[idx] + recursion2(idx - 2, nums)
            notPick = recursion2(idx - 1, nums)
            
            t2[idx] = max(pick, notPick)
            return t2[idx]
        
        maxx = max(recursion1(len(nums[1:])-1, nums[1:]), recursion2(len(nums[:-1])-1, nums[:-1]))
        return maxx