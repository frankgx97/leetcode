# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        1 pass - ac
        use prev and nex pointer to store the previous and next node of current node
        edge cases:
        - head is none
        - only one node
        - 
        '''
        if not head:
            return None
        
        prev = None
        current = head
        nex = None
        while current:
            nex = current.next
            current.next = prev
            prev = current
            current = nex
        return prev
