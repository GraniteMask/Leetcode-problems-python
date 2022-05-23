class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) >= 2 and len(nums) <= 10000 and target >= -1000000000 and target <=1000000000:
            for i in range(len(nums)-1):
                for j in range(i+1, len(nums)):
                    if nums[i]+nums[j] == target:
                        if nums[i] >= -1000000000 and nums[i] <=1000000000:
                            return i,j