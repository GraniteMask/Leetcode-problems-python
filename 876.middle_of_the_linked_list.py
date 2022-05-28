# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = 0
        count = 0
        
        node = head
        
        while head is not None:
            length += 1
            head = head.next
        
        mid = length // 2
        print(mid)
        
        while node is not None:
            print(head)
            if count == mid:                
                return node
            else:
                count += 1
                node = node.next
        return node
                
        