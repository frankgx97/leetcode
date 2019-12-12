# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        bfs with queue
        '''
        def bfs(root):
            if not root:
                return []
            queue = [root]
            r = []
            while queue:
                innerqueue = []
                for i in queue:
                    innerqueue.append(i)
                queue = []
                curr = []
                for i in innerqueue:
                    curr.append(i.val)
                    if i.left:
                        queue.append(i.left)
                    if i.right:
                        queue.append(i.right)
                r.append(curr)
            return r
        return bfs(root)
