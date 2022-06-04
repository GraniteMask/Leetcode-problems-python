"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        tempCopy = {None: None} # None declared for the condition cur.next = None
        
        cur = head
        
        while cur:
            copy = Node(cur.val)
            tempCopy[cur] = copy
            cur = cur.next
            
        # print(tempCopy)
        cur = head
        
        while cur:
            copy = tempCopy[cur]
            copy.next = tempCopy[cur.next]            # this cur.next and random coming from cur of this while loop
            copy.random = tempCopy[cur.random]
            cur = cur.next
        
        return tempCopy[head]