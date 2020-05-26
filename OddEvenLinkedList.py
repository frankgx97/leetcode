# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        oddhead = ListNode(0)
        evenhead = ListNode(0)
        oddcurr = oddhead
        evencurr = evenhead
        curr = head
        i = 1
        while curr:
            if i%2 == 0:
                evencurr.next = curr
                evencurr = evencurr.next
            else:
                oddcurr.next = curr
                oddcurr = oddcurr.next
            curr = curr.next
            i+=1
        oddcurr.next = evenhead.next
        evencurr.next = None
        return oddhead.next
