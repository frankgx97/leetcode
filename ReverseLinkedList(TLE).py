# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import copy

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        tail = None
        current = head
        next = None
        if current != None:
            tail = copy.deepcopy(current)
            tail.next = None
            current = current.next
        while current != None:
            next = copy.deepcopy(current.next)
            current.next = tail
            tail = current
            current = next
        return tail
        
