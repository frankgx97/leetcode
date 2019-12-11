# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        '''
        hashset & in order traversal - ac
        time: O(n)
        space: O(n)
        '''
        hashset = set()
        def trav(root):
            if not root:
                return False
            l = trav(root.left)
            if k - root.val in hashset:
                return True
            else:
                hashset.add(root.val)
            r = trav(root.right)
            return l or r
        return trav(root)
