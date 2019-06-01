# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack = [root]
        current = root
        result = []
        while current.left:
            stack.append(current.left)
            current = current.left
        while stack:
            t = stack.pop()
            result.append(t.val)
            t = t.right
            while(t):
                stack.append(t)
                t = t.left
        return result
