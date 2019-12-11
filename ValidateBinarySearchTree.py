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
        in each recursiom, carry a min value and a max value, compare min and max with current node, if current value <= min or >= max, return false
            10
           /  \
          5   15
              / \
             6  20
        at 10, min = -inf, max = inf
        at 5, min = -inf, max = 10(when traveling the left subtree, we care about if nodes in the left subtree is larger than the max, so we only update max)
        at 15, min = 10, max = inf
        at 6, min = 10, max = 15, 6 < min, return False
            
        time: O(n)
        ref: https://leetcode.com/problems/validate-binary-search-tree/discuss/445879/Python-easy-to-understand-solution
        '''
        def trav(root,mi,ma):
            if not root:
                return True
            if root.val <= mi or root.val >= ma:
                return False
            
            return trav(root.left,mi,root.val) and trav(root.right, root.val,ma)
        return trav(root,float('-inf'),float('inf'))
            
