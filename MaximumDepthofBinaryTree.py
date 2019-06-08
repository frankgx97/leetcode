# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    maxm = 0
    def maxDepth(self, root: TreeNode) -> int:
        self.maxm = 0
        self.trav(root,1)
        return self.maxm
        
    def trav(self, root,depth):
        if not root:
            return
        if depth > self.maxm:
            self.maxm = depth
        self.trav(root.left, depth+1)
        self.trav(root.right, depth+1)
        return
        
        
