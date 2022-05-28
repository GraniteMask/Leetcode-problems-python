# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        nodeMain = ListNode()
        node = nodeMain
        
        print(nodeMain, node)
        
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
                
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
            
            print('MAIN', nodeMain)
            print ('TAIL', node)
        
        if list1:
            node.next = list1
        elif list2:
            node.next = list2
        
        print(node.next)
        return nodeMain.next
                