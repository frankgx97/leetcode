# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        '''
        recursive merge sort - ac
        ref: https://blog.csdn.net/m0_37324740/article/details/80762974
        
        divide:
        - use fast-slow pointers to determine the middle of the list (break the list before the slow pointer, slow pointer is pointing to the start of the 2nd part of the list.)
        conquer:
        - ref: https://leetcode.com/problems/merge-two-sorted-lists/
        '''
        def merge(l1,l2):
            dummy = ListNode(-1)
            current = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            if l1:
                current.next = l1
            else:
                current.next = l2
            return dummy.next
        
        def ms(start):
            if not start or not start.next:
                return start
            fast, slow, prev = start, start, None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            l = ms(start)
            r = ms(slow)
            return merge(l,r)
        return ms(head)
