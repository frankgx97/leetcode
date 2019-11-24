# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        s = 0
        def trav(root):
            nonlocal s
            if not root:
                return
            if root.val >= L and root.val <= R:
                s += root.val
            if root.val >= L:
                trav(root.left)
            if root.val <= R:
                trav(root.right)
            
        trav(root)
        return s
