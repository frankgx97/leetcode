# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    result = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []
        return self.traversal(root)
    
    def traversal(self, root):
        if root == None:
            return []
        self.traversal(root.left)
        self.result.append(root.val)
        self.traversal(root.right)
        return self.result
