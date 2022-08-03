# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        global pArr
        global qArr
        
        pArr = []
        qArr = []
        
        def traversep(root):
            
            global pArr
            
            if root is None:
                pArr.append(None)
                return
            
            pArr.append(root.val)
            
            traversep(root.left)
            traversep(root.right)
            
        def traverseq(root):
            
            global qArr
            
            if root is None:
                qArr.append(None)
                return
            
            qArr.append(root.val)
            
            traverseq(root.left)
            traverseq(root.right)
            
        traversep(p)
        traverseq(q)
        
        
        if pArr == qArr:
            return True
        else:
            return False