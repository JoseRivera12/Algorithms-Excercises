
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # recursive approach
        # if root:
        #     root_val = root.val

        #     p_val = p.val
        #     q_val = q.val
        
        #     if p_val > root_val and q_val > root_val:
        #         return self.lowestCommonAncestor(root.right, p, q)
        #     if p_val < root_val and q_val < root_val:
        #         return self.lowestCommonAncestor(root.left, p, q)
        #     else:
        #         return root
        
        # iterative approach
        p_val = p.val
        q_val = q.val
        node = root

        while node:
            root_val = node.val        
            if p_val > root_val and q_val > root_val:
                node = node.right
            elif p_val < root_val and q_val < root_val:
                node = node.left
            else:
                return node
