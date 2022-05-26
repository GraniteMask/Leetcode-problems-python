# Brute

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
             
        for i in range(len(nums)):
            count = 0
            for j in range(i+1, len(nums)):
                if nums[j] == nums[i]:
                    count += 1
            
            if count == len(nums) // 2:
                return nums[i]

# More Efficient solution

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
             
        nums.sort()
            
        return nums[len(nums)//2]