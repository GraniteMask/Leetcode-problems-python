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

# More Efficient solution - Time complexity O(nlogn) and space complexity O(n) - Tim sort

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
             
        nums.sort()
            
        return nums[len(nums)//2]

# Solution with O(1) space complexity       
 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
             
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)