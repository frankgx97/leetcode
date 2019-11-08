# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        '''
        manipulate pointers - ac
        use a helper function to reverse list of selected range, returns the head and tail node after reversion
        then iterate the list, find the node that is before the reverse head, after the reverse tail, and start the reverse.
        then connect the nodes together
        use dummy head to handle modification to head node
        '''
        def rev(h,c):
            i=0
            prev = None
            current = h
            nex = None
            while i<=c:
                nex = current.next
                current.next = prev
                prev = current
                current = nex
                i+=1
            return prev,h #head and tail after reversion
                
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        
        i=0
        current = dummy
        prev = dummy
        
        before_head = None
        after_tail = None
        start_rev = None
        
        while current:
            if i == m:
                before_head = prev
                start_rev = current
            if i == n:
                after_tail = current.next
            i+=1
            prev = current
            current = current.next
        before_head.next, tail = rev(start_rev, n-m)
        tail.next = after_tail
        return dummy.next
