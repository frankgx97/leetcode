# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:
            return 0
        return self.trav(root, 0,sum, 0) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        
    def trav(self, root, ss, target, r):
        if root == None:
            return r
        if ss+root.val == target:
            f = 1
        else:
            f = 0
        return f + self.trav(root.left, ss+root.val, target, r) + self.trav(root.right, ss+root.val, target, r)
