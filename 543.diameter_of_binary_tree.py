# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        global res 
        res = 0
        
        def dfs(root):
            global res
            
            if root is None:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            res = max(res, 2 + left + right)   # Diameter
            
            return 1 + max(left,right)         # Height each node
        
        dfs(root)
        return res