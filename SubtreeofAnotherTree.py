# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        '''
        recursive - ac
        time: O(mn)
        space: O(height of tree)
        ref: is same tree
        '''
        def is_same(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return is_same(p.left,q.left) and is_same(p.right,q.right)
        
        def trav(root,t,r):
            if not root:
                return r
            if is_same(root,t):
                r = True
            return trav(root.left,t,r) or trav(root.right,t,r)
        
        return trav(s,t,False)
