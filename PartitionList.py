# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        new_dummy = ListNode(-1)
        new_current = new_dummy
        
        dummy = ListNode(99999)
        dummy.next = head
        current = dummy
        while current != None and current.next != None:
            if current.next.val < x:
                new_current.next = ListNode(current.next.val)
                new_current = new_current.next
                current.next = current.next.next
            else:
                current = current.next
        new_current.next = dummy.next
        return new_dummy.next
