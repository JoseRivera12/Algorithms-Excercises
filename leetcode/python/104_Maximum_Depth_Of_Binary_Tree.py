# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # initial approach recursive DFS
        # if not root:
        #     return 0
        
        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)

        # return max(left, right) + 1

        # improved version iterative DFS using a stack
        # stack = []
        # if root:
        #     stack.append((root, 1))
        
        # depth = 0
        # while stack:
        #     node, curr_depth = stack.pop()
        #     if node is not None:
        #         depth = max(depth, curr_depth)
        #         stack.append((node.left, curr_depth + 1)) 
        #         stack.append((node.right, curr_depth + 1))
            
        # return depth
        # BFS version
        queue = deque()
        if root:
            queue.append((root, 1))
        
        max_depth = 0
        while queue:
            curr, depth = queue.popleft()
            max_depth = max(max_depth, depth)

            if curr.left:
                queue.append((curr.left, depth+1))
            if curr.right:
                queue.append((curr.right, depth+1))

        return max_depth



        
