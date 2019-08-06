# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current != None and current.next != None:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
