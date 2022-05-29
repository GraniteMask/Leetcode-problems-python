# BRUTE-FORCE SOLUTION USING ARRAY - O(n) space complexity

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []
        
        while head is not None:
            array.append(head.val)
            head = head.next
            
        l, r = 0, len(array) -1
        
        while l <= r:
            if array[l] != array[r]:
                return False
            
            l += 1
            r -= 1
            
            
        return True


# OPTIMIZED TECHNIQUE - O(n) time and O(1) space complexities