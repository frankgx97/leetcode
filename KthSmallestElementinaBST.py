# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
        in order traversal of bst is sorted
        '''
        
        n = 0
        target = -1
        
        def trav(root):
            nonlocal n
            nonlocal target
            if not root:
                return
            
            trav(root.left)
            n+=1
            if n == k:
                target = root.val
            trav(root.right)
            return
        trav(root)
        return target
