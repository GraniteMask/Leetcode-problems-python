class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = (target + sum(nums))//2
        
        t = [[0]*(int(s)+1) for i in range(len(nums)+1)]
        
        if len(nums) == 1:
            if abs(nums[0]) != abs(target):
                return 0
            else:
                return 1
            
        if (target + sum(nums)) % 2 != 0: return 0
            
        
        
        for i in range(len(nums)+1):
            for j in range(int(s)+1):
                if i == 0:
                    t[i][j] = 0
                if j == 0:
                    t[i][j] = 1
            
        for i in range(1, len(nums)+1):
            for j in range(int(s)+1):
                
                if nums[i-1] <= j:
                    t[i][j] = t[i-1][j-nums[i-1]] + t[i-1][j]
                
                elif nums[i-1] > j or nums[i-1] == 0:
                    t[i][j] = t[i-1][j]
        
        return t[len(nums)][s]