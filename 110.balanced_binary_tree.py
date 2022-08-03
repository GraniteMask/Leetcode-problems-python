# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        global res
        res = True
        
        def dfs(root):
            global res
            
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if abs(right - left) > 1:
                res = False
                
            return 1 + max(left, right)
            
            
        dfs(root)
        
        return res
        
    