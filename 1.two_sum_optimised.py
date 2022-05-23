class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for i in range(len(nums)):
            if target-nums[i] in res: return [res[target-nums[i]], i]
            else: res[nums[i]] = i
        return 0