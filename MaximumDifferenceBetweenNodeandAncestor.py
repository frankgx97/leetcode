# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        '''
        recursive - ac
        pass the max and min number in to next recursion
        if current value is larger than a, update a and max diff
        if current value is smaller than b, update b and max diff
        '''
        _max = 0
        
        def trav(root,a,b):
            nonlocal _max
            if not root:
                return
            if a == None or b == None:
                a,b = root.val,root.val
            
            if root.val > a:
                a = root.val
                _max = max(_max,abs(a-b))
            if root.val < b:
                b = root.val
                _max = max(_max,abs(a-b))
            
            trav(root.left,a,b)
            trav(root.right,a,b)
            return
        
        trav(root,None,None)
        return _max
