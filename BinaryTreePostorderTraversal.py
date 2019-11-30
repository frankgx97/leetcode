# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        ac
        recursive - trivial
        iterative - do a normal iterative dfs(preorder)
        then reverse the output
        complexity: O(n) (each node visited once)
        '''
        '''
        #recursive
        def trav(root):
            if not root:
                return
            trav(root.left)
            trav(root.right)
            r.append(root.val)
            return
        r = []
        trav(root)
        return r
        '''
        #iterative
        
        stack = [root]
        r = []
        if not root:
            return []
        while stack:
            curr = stack.pop(-1)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
            r.append(curr.val)
        return r[::-1]
