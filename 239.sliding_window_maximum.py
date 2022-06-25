# Brute force - limited test cases passed
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        largest = []
        
        for i in range(len(nums)):
            maximum = nums[i]
            if i + (k-1) < len(nums):
                for j in range(i, i+k):
                    maximum = max(maximum, nums[j])
                
                largest.append(maximum)
            
        return largest
            