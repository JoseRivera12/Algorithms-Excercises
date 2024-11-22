# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isequal(node, subnode) -> bool:
            if not node and not subnode:
                return True
            
            if not node or not subnode:
                return False
            
            return ((node.val == subnode.val) and
                isequal(node.left, subnode.left) and
                isequal(node.right, subnode.right))
        
        def dfs(node):
            if not node:
                return False
            
            elif isequal(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
