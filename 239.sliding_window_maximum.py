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
            
# Optimized solution - O(n) time complexity

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        q = collections.deque()  # stores index
        l = r = 0
        
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # remove left value from window
            if l > q[0]:
                q.popleft()
                
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
            
        return output
            