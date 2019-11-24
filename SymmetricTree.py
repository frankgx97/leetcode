# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        invert one subtree of root(ref https://leetcode.com/problems/invert-binary-tree/)
        then compare if l subtree and r subtree are the same(ref https://leetcode.com/problems/same-tree/)
        '''
        def rev(root):
            if not root:
                return
            temp = root.left
            root.left = root.right
            root.right = temp
            rev(root.left)
            rev(root.right)
            return
        def issame(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return issame(t1.left,t2.left) and issame(t1.right,t2.right)
        if not root:
            return True
        rev(root.right)
        return issame(root.left,root.right)
