# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        '''
        dfs
        ref: https://leetcode.com/problems/house-robber-iii/discuss/79437/C%2B%2B-JAVA-PYTHON-and-explanation
        
        f1(node) be the value of maximum money we can rob from the subtree with node as root ( we can rob node if necessary).

        f2(node) be the value of maximum money we can rob from the subtree with node as root but without robbing node.

        Then we have

        f2(node) = f1(node.left) + f1(node.right) and

        f1(node) = max( f2(node.left)+f2(node.right)+node.value, f2(node) ).
        '''
        def dfs(node):
            if node is None:
                return (0,0)
            l = dfs(node.left)
            r = dfs(node.right)
            f1 = l[1] + r[1]
            f2 = max(l[1] + r[1], l[0] + r[0] + node.val)
            return (f1,f2)
        return dfs(root)[1]
