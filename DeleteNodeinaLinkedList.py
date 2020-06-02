# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        print(node.val)
        prev = None
        while node.next:
            node.val = node.next.val
            if not prev:
                prev = node
            else:
                prev = prev.next
            node = node.next
        prev.next = None
        return
