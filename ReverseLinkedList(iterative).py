# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        tail = None
        current = head
        next = None
        while current != None:
            next = current.next
            current.next = tail
            tail = current
            current = next
        return tail
        
