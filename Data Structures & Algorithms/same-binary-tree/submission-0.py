# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isSame = True

        def dfs(root1, root2):
            nonlocal isSame

            # Case 1: both are None → same
            if not root1 and not root2:
                return

            # Case 2: one is None → not same
            if not root1 or not root2:
                isSame = False
                return

            # Case 3: both exist → compare values
            if root1.val != root2.val:
                isSame = False

            # Check children
            dfs(root1.left, root2.left)
            dfs(root1.right, root2.right)

        dfs(p, q)
        return isSame

            


            
