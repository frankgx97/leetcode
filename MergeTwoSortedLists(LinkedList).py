# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        dummy = ListNode(-9999)
        dummy.next = head
        current = dummy
        
        while l2 != None:
            while current != None:                    
                if l2.val >= current.val and (current.next == None or l2.val < current.next.val):
                    temp = current.next
                    current.next = ListNode(l2.val)
                    current.next.next = temp
                    break
                else:
                    current = current.next
            l2 = l2.next
        return dummy.next
