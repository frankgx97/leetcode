# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        recursive - ac
        recursively check if all child nodes of every node is smaller/larger than it's value.
        complexity O(n^2)
        '''
        def left_smaller_than_root(root, val):
            if not root:
                return True
            if root.val >= val:
                return False
            return left_smaller_than_root(root.left, val) and left_smaller_than_root(root.right, val)
            
        def right_larger_than_root(root,val):
            if not root:
                return True
            if root.val <= val:
                return False
            return right_larger_than_root(root.left, val) and right_larger_than_root(root.right, val)
            
        
        def valid(root):
            if not root:
                return True
            if not (left_smaller_than_root(root.left, root.val) and right_larger_than_root(root.right,root.val)):
                return False
            return valid(root.left) and valid(root.right)
        return valid(root)
