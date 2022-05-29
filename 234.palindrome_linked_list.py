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


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        fast = head
        slow = head
        
        # find middle(slow)
        
        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            
        
        # Reversing the linked list
        
        prev = None
        
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            
        # check palindrome
        
        left, right = head, prev
        
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True
            