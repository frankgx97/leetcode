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
        
        def merge(p1,p2):
            dummy = ListNode(-1)
            curr = dummy
            
            while p1 or p2:
                if not p1:
                    curr.next = p2
                    break
                elif not p2:
                    curr.next = p1
                    break
                    
                if p1.val <= p2.val:
                    curr.next = p1
                    p1 = p1.next
                else:
                    curr.next = p2
                    p2 = p2.next
                curr = curr.next
            return dummy.next
            
            
        def ms(start):
            if not start or not start.next:
                return start
            
            p1,p2 = start,None
            
            slow, start, prev = start, start, None
            
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
                
            prev.next = None
            
            l = ms(start)
            r = ms(slow)
            
            return merge(l,r)
        
        return ms(head)
                
            
