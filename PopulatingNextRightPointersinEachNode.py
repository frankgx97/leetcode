"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

'''
bfs - ac
use counter to find the last value in the current level and exclude it.
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = [root]
        counter = 1
        prev = None
        while q:
            counter -= 1
            current = q.pop(0)
            #print(current.val)
            if current.left and current.right:
                q.append(current.left)
                q.append(current.right)
            if prev:
                #print(prev.val,"->",current.val)
                prev.next = current
            prev = current
            if counter == 0:
                #print('last')
                current.next = None
                counter = len(q)
                prev = None
        return root
