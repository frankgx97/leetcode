# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        ac
        recursive and iterative
        caution: right child goes first in iterative approach (stack is first in last out)
        '''
        r = []
        #recursive dfs
        def trav(root):
            if not root:
                return
            r.append(root.val)
            trav(root.left)
            trav(root.right)
            return
        
        #iterative dfs
        def trav_iter(root):
            if not root:
                return []
            stack = [root]
            r = []
            while stack:
                curr = stack.pop(-1)
                # stack is first in last out, push right child into stack first
                if curr.right:
                    stack.append(curr.right)
                r.append(curr.val)
                if curr.left:
                    stack.append(curr.left)
            return r
        return trav_iter(root)
