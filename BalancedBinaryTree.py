# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        ac
        balance: the height of left and right subtree do not differ more than 1
        ref: https://leetcode.com/problems/diameter-of-binary-tree/
        '''
        res = True
        def height(root):
            nonlocal res
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            if abs(l-r)>1:
                res = False
            return max(l,r)+1
        height(root)
        return res
            
