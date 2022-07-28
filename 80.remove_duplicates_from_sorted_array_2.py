class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        length = 2
        i = 2
        
        while i < len(nums):
            if (nums[i]!=nums[length-2]) :
                nums[length] = nums[i]
                length+=1
                
            i += 1
        return(length)

                