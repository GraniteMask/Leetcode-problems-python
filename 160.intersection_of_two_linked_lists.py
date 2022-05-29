# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = 0
        curr = headA
        while curr is not None : 
            curr = curr.next
            l1 += 1
        l2 = 0
        curr = headB
        while curr is not None :
            curr = curr.next
            l2 += 1
        if l1 < l2 :
            for i in range(l2-l1):
                headB = headB.next
        elif l1 > l2 :
            for i in range(l1-l2):
                headA = headA.next
        while headA is not None and headB is not None :
            if headA==headB:
                return headA
            else :
                headA = headA.next
                headB = headB.next   
        return None