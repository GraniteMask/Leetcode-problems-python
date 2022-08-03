# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def traverse(root, count):
            
            if root is None:
                return count
            
            return max(traverse(root.left, count+1), traverse(root.right, count+1))
        
        return traverse(root, 0)
            