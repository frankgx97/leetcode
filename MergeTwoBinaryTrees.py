# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        '''
        recursive
        use t1 as base
        for each node, if t1.left/right child do not exist but t2.left/right child exist,
        point the pointer to the node of t2
        traverse the subtree and mark all nodes and visited to avoid being sumed up again.
        '''
        added = set()
        def travadd(r):
            if not r:
                return
            added.add(r)
            travadd(r.left)
            travadd(r.right)
            return
        
        def merge(st1,st2):
            if not st1 or not st2:
                return
            if st1 and st2 and (st1 not in added and st2 not in added):
                st1.val = st1.val + st2.val
            if not st1.left and st2.left:
                st1.left = st2.left
                travadd(st1.left)
            if not st1.right and st2.right:
                st1.right = st2.right
                travadd(st1.right)
            merge(st1.left,st2.left)
            merge(st1.right,st2.right)
            
        dummy1 = TreeNode(-1)
        dummy1.left = t1
        dummy2 = TreeNode(-1)
        dummy2.left = t2
        merge(dummy1,dummy2)
        return dummy1.left
