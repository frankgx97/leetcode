# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        '''
        buttom-up recursive - ac
        in each recursion, calculate current the sum with lsum+rsum+current.val
        calculate the current node count with lnode+rnode+1
        '''
        av = 0
        r = []
        def trav(root):
            nonlocal av
            if not root:
                return (0,0)
            lsum,lnode = trav(root.left)
            rsum,rnode = trav(root.right)
            currsum = lsum+rsum+root.val
            currnode = lnode+rnode+1
            av = max(av,currsum/currnode)
            return (currsum,currnode)
        trav(root)
        return av
