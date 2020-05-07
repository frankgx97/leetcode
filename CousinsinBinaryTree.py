# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xd = yd = xp = yp = 0
        def trav(root,parent,depth):
            nonlocal xd,yd,xp,yp
            if not root:
                return
            if root.val == x:
                xd = depth
                xp = parent.val if parent else 0
            if root.val == y:
                yd = depth
                yp = parent.val if parent else 0
            trav(root.left, root, depth+1)
            trav(root.right, root, depth+1)
            return
        trav(root, None, 0)
        if xd == yd and xp != yp:
            return True
        else:
            return False
                
        
