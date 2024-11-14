
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     # my solution
    #     if not root:
    #         return True
    #     return (
    #         abs(self.dfs(root.right) - self.dfs(root.left)) < 2
    #         and self.isBalanced(root.left)
    #         and self.isBalanced(root.right))

    # def dfs(self, root) -> int:
    #     if not root:
    #         return -1
    #     return  1 + max(self.dfs(root.right), self.dfs(root.left))
    
    # optimal
    # instead of recalculating calling again self.isBalanced i check it in dfs
    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1

        # Check subtrees to see if they are balanced.
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0

        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(
            leftHeight, rightHeight
        )

    def isBalanced(self, root: TreeNode) -> bool:
        print(self.isBalancedHelper(root)[1])
        return self.isBalancedHelper(root)[0]
