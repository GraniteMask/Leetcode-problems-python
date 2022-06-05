class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision top include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            #decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
            
            
        dfs(0)
        return res
    
# I struggled with understanding the reason for appending `subset.copy()` instead of `subset`.
#I think what is happening is, we need to append the actual instance of each modified subset `subset.copy()` instead of the reference which is pointing to the subset which gets modified. 
