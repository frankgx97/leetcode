# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        op = dummy
        count = 0
        
        while True:
            if current.next == None:
                op.next = op.next.next
                break
            else:
                current = current.next
                if count >= n:
                    op = op.next
                count += 1
                
        return dummy.next
