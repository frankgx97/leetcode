# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swap(node):
            if not node.next.next:
                return node
            
            out = node.next.next.next
            first = node.next
            second = node.next.next
            first.next = out
            second.next = first
            node.next = second
            return node
            
            
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next != None:
            swap(current)
            if current.next.next:
                current = current.next.next
            else:
                break
        return dummy.next
            
        
        
