class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = 0
        
        for i in nums:
            s =  s + i
        
        print(s)
        
        t = [[False]*(int(s/2)+1) for i in range(len(nums)+1)]
        
        if s % 2 != 0:
            return False
        elif s % 2 == 0:
            for i in range(len(nums)+1):
                for j in range(int(s/2)+1):
                    if i == 0:
                        t[i][j] = False
                    if j == 0:
                        t[i][j] = True
                        
            for i in range(1, len(nums)+1):
                for j in range(1, int(s/2+1)):
                    
                    if nums[i-1] <= j:
                        t[i][j] = t[i-1][j-nums[i-1]] or t[i-1][j]
                        
                    else:
                        t[i][j] = t[i-1][j]
            return t[len(nums)][int(s/2)]