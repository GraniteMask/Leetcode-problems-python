# Running in O(log n) time complexity and O(1) space complexity

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            check_if_halves_are_even = (right - mid) % 2 == 0
            if nums[mid + 1] == nums[mid]:
                if check_if_halves_are_even:
                    left = mid + 2
                else:
                    right = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if check_if_halves_are_even:
                    right = mid - 2
                else:
                    left = mid + 1
            else:
                return nums[mid]
        return nums[left]