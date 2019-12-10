# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        '''
        linked list deletion with dummy head - ac
        corner case:
        [1,1],1
        only forward current pointer when not removing items
        '''
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
        
