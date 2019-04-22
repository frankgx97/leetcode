# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lst = []
        current = head
        while True:
            lst.append(current)
            if current.next == None:
                break
            else:
                current = current.next

        if len(lst)-n-1 < 0:
            head = head.next
            return head
        else:
            lst[len(lst)-n-1].next = lst[len(lst)-n-1].next.next
            return head
