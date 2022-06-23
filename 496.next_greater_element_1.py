# Brute force method - O(n^2) solution

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j] > nums1[i] and nums2.index(nums2[j]) > nums2.index(nums1[i]):
                    output.append(nums2[j])
                    break
                
            if len(output) != i+1:
                output.append(-1)
                       
        return output
                     
# Optimized method - O(m+n) solution

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1Idx = {n:i for i, n in enumerate(nums1)}
        res = [-1]*len(nums1)
        
        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return res