# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        set - ac
        use a set to store the reference of visited nodes
        '''
        v = set()
        current = head
        while current != None:
            if current in v:
                return current
            else:
                v.add(current)
                current = current.next
        return None
