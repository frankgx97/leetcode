# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        stack - ac
        use stack to store ref of nodes
        O(n) space, O(n) time
        '''
        if not head:
            return None
        current = head
        stack = []
        while current:
            stack.append(current)
            current = current.next
        head = stack[-1]
        current = head
        while len(stack) > 0:
            current.next = stack[-1]
            stack.pop(-1)
            current = current.next
        current.next = None
        return head
