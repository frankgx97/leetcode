# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
        recursive - ac
        use the mid of the array as root
        left part for the l subtree
        right part for the r subtree
        '''
        def bst(arr):
            if not arr:
                return
            mid = len(arr)//2
            rootval = arr[mid]
            lsub = arr[:mid]
            rsub = arr[mid+1:]
            root = TreeNode(rootval)
            root.left = bst(lsub)
            root.right = bst(rsub)
            return root
        return bst(nums)
