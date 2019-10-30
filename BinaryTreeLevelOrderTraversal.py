# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def bfs(root):
            q = [root]
            counter = len(q)
            temp = []
            result = []
            direction = True
            while len(q) > 0:
                curr = q[0]
                q.pop(0)
                if curr:
                    temp.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)

                counter -= 1
                if counter == 0:
                    direction = not direction
                    counter = len(q)
                    if len(temp) > 0:
                        result.append(temp)
                    temp = []
            return result
                    
        return bfs(root)
