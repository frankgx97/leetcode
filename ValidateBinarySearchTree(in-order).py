# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        in order traversal - ac
        do a in order traversal, find if it is mono increase
        '''
        r = []
        def isbst(root):
            if not root:
                return
            isbst(root.left)
            r.append(root.val)
            isbst(root.right)
            return
        
        isbst(root)
        curr = -math.inf
        for i in r:
            if i <= curr:
                return False
            curr = i
        return True
