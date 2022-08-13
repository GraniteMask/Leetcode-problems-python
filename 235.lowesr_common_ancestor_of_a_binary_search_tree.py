# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def traverse(root, p, q):
            if not root:
                return 
            curr = root.val

            if curr < p.val and curr < q.val:
                return traverse(root.right, p, q)
            elif curr > p.val and curr > q.val:
                return traverse(root.left, p, q)
            else:
                return root
            
        return traverse(root, p, q)