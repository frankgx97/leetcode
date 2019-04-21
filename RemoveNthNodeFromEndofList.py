# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head
        length = 0
        while True:
            length += 1
            if current.next == None:
                break
            else:
                current = current.next
        
        current = head
        for i in range(0,length):
            if i == length-n-1:
                current.next = current.next.next
                break
            elif length == n:
                head = head.next
                break
            if current.next == None:
                break
            else:
                current = current.next
        return head
