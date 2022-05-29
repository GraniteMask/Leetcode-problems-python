# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        
        while l1 or l2 or carry:      # carry to avoid edge case like 7 + 8 = 15 where carry 1 would be neglected if this condition is not present
            
            v1 = l1.val if l1 else 0   # else 0 condition is to prevent cases where if the any of the two number is bigger and another is smaller in terms of digit then 0  will be present as placeholder in the smaller number to equate its digits to bigger one
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next