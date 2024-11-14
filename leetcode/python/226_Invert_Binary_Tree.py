# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# I need to move:
# left into right
# right into left 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # initial solution
        # def invert(root):
        #     if root:
        #         root.left, root.right = root.right, root.left
        #         invert(root.left)
        #         invert(root.right)
        # invert(root)
        # return root
        # second approach
        # if not root:
        #     return
        # right = self.invertTree(root.right)
        # left = self.invertTree(root.left)
        # root.left = right
        # root.right = left
        # return root
        # BFS
        if not root:
            return None
        
        queue = collections.deque([root])
        while queue:
            curr = queue.popleft()
            curr.left, curr.right = curr.right, curr.left
            
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)
            
            
            
        return root
