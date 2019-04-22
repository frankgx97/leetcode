# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        lst = []
        current = dummy
        
        while True:
            lst.append(current)
            if current.next == None:
                break
            else:
                current = current.next

        lst[len(lst)-n-1].next = lst[len(lst)-n-1].next.next
        return dummy.next
