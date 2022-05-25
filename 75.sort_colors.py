# Brute - Swapping approach

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,-1,-1):
            for j in range(i-1,-1,-1):
                if(nums[i]<nums[j]):
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    print(nums)