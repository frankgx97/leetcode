# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        for i in preorder[1:]:
            curr = root
            while True:
                if i <= curr.val:
                    if not curr.left:
                        curr.left = TreeNode(i)
                        break
                    else:
                        curr = curr.left
                        continue
                else:
                    if not curr.right:
                        curr.right = TreeNode(i)
                        break
                    else:
                        curr = curr.right
                        continue
        return root
