# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
bfs level order traversal with hashtable - ac
use bfs, not dfs

   3=0
  /\
 /  \
9=-1  20=1
    /\
   /  \
  15=0 7=2 


'''
import heapq
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [(root,0)]
        dic = {}
        while queue:
            currv,currk = queue.pop(0)
            if currk not in dic:
                dic[currk] = [currv.val]
            else:
                dic[currk].append(currv.val)
            if currv.left:
                queue.append((currv.left,currk-1))
            if currv.right:
                queue.append((currv.right,currk+1))
        r = []
        heap = []
        for i in dic:
            heapq.heappush(heap,(i,dic[i]))
        while heap:
            r.append(heapq.heappop(heap)[1])
        return r


'''
failed dfs solution - nodes with lower depth comes first

import heapq
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        dic = {}
        def trav(root,k):
            if not root:
                return
            if k not in dic:
                dic[k] = [root.val]
            else:
                dic[k].append(root.val)
            trav(root.left,k-1)
            trav(root.right,k+1)
            return
        trav(root,0)
        r = []
        heap = []
        for i in dic:
            heapq.heappush(heap,(i,dic[i]))
        while heap:
            r.append(heapq.heappop(heap)[1])
        return r
'''     
        
