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
        '''
        def is_larger_than_root(root,v):
            if not root:
                return False
            if root.val >= v:
                return True
            return is_larger_than_root(root.left,v) or is_larger_than_root(root.right,v)
        
        def is_smaller_than_root(root,v):
            if not root:
                return False
            if root.val <= v:
                return True
            return is_smaller_than_root(root.left,v) or is_smaller_than_root(root.right,v)
            
            
        def isbst(root):
            if not root:
                return True
            if root.left and (root.left.val >= root.val or is_larger_than_root(root.left,root.val)):
                return False
            if root.right and (root.right.val <= root.val or is_smaller_than_root(root.right,root.val)):
                return False
            return isbst(root.left) and isbst(root.right)
        return isbst(root)
