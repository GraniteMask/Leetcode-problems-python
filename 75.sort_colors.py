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

# Optimized Solution

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0, len(nums)-1
        i=0
        
        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        while i<=r:
            if nums[i] == 0:
                swap(l,i)
                l +=1
            elif nums[i] == 2:
                swap(i,r)
                r-=1
                i-=1  #this is used so that i increment effect is cancel out as we don't want to increment i when we find nums[i] == 2
            i += 1
                