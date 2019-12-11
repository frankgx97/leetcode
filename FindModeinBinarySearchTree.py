# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        '''
        hashtable - ac
        time O(nlogn)
        space O(n)
        '''
        dic = {}
        def trav(root):
            if not root:
                return
            trav(root.left)
            if root.val not in dic:
                dic[root.val] = 1
            else:
                dic[root.val] += 1
            trav(root.right)
            return
        if not root:
            return []
        trav(root)
        heap = []
        for i in dic.keys():
            heapq.heappush(heap,(-dic[i],i))
        ma = heap[0][0]
        r = []
        while heap and heap[0][0] == ma:
            r.append(heapq.heappop(heap)[1])
        return r
        
            
