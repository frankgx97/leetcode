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
        self.res = 0
        self.t(root, sum)
        return self.res
    
    def t(self, root, sum):
        if root == None:
            return
        self.trav(root,0,sum)
        self.t(root.left,sum)
        self.t(root.right,sum)
        return
        
    def trav(self, root, sum, target):
        if root == None:
            return
        if sum+root.val == target:
            self.res += 1
        self.trav(root.left, sum+root.val, target)
        self.trav(root.right, sum+root.val, target)
        return
        
