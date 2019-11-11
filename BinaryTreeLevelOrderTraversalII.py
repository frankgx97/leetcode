# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        '''
        level order traversal and reverse - ac
        level order traverse the tree, use a counter to seperate levels
        reverse the result before returning.
        '''
        if not root:
            return []
        r = []
        temp = []
        q = [root]
        counter = 1
        while len(q)>0:
            temp.append(q[0].val)
            counter -= 1
            if q[0].left:
                q.append(q[0].left)
            if q[0].right:
                q.append(q[0].right)
            q.pop(0)
            if counter == 0:
                counter = len(q)
                r.append(temp)
                temp = []
        if len(temp) > 0:
            r.append(temp)
        return reversed(r)
