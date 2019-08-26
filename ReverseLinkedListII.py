# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
            
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        
        if m == n:
            return dummy.next
        
        i=0
        current = dummy
        prev = dummy
        
        while current:
            if i == m:
                start = current
                left = prev
            if i == n:
                end = current
                right = current.next
            current = current.next
            if i>=1:
                prev = prev.next     

            i += 1
            
        current = start.next
        prev = start
        end.next = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        left.next = end
        start.next = right
            
        return dummy.next
