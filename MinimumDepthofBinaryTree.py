# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''
        dfs - ac
        pay attention the case that left or right child do not exist
        we should exclude the child depth with the same value as the parent depth.
        '''
        def trav(root,depth):
            if not root:
                return depth-1
            l = trav(root.left, depth+1)
            r = trav(root.right,depth+1)
            #print(root.val,l,r)
            if l == depth:
                return r
            elif r == depth:
                return l
            else:
                return min(l,r)
        return trav(root,1)
