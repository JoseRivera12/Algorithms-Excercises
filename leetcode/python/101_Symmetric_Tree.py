
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # DFS solution
        # def dfs(node_1, node_2) -> bool:
        #     if not node_1 and not node_2:
        #         return True

        #     if not node_1 or not node_2:
        #         return False
            
        #     return (node_1.val == node_2.val and 
        #         dfs(node_1.left, node_2.right) and
        #         dfs(node_1.right, node_2.left))
        
        # return dfs(root.left, root.right)
        # BFS solution
        queue = deque()
        queue.append(root)
        queue.append(root)

        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)

        return True

            
