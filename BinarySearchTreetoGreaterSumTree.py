# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        '''
        two pass inorder recursive - ac
        first pass calc the sum of the bst
        second pass modify the current value to total sum - current sum
        in order traversal of bst is sorted
        '''
        treesum = 0
        def getsum(root):
            nonlocal treesum
            if not root:
                return
            getsum(root.left)
            treesum += root.val
            getsum(root.right)
            return 
        
        currentsum = 0
        def trav(root):
            nonlocal currentsum
            if not root:
                return
            trav(root.left)
            rtval = root.val
            root.val = treesum - currentsum
            currentsum += rtval
            trav(root.right)
            return
        
        getsum(root)
        trav(root)
        return root
