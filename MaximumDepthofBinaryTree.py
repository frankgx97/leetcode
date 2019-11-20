# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
        dfs - ac
        '''
        def trav(root,depth):
            if not root:
                return depth
            l = trav(root.left, depth+1)
            r = trav(root.right,depth+1)
            return max(l,r)
        return trav(root,0)
