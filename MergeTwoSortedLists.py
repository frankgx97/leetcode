# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def assembleList(self,l):
        former = None
        first = None
        for i in l:
            current = ListNode(i)
            if former == None:
                former = current
                first = current
            else:
                former.next = current
                former = current
        return first
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        
        while l1 != None:
            result.append(l1.val)
            if l1.next != None:
                l1 = l1.next
            else:
                break
        
        while l2 != None:
            result.append(l2.val)
            if l2.next != None:
                l2 = l2.next
            else:
                break
        
        result.sort()
        return self.assembleList(result)
        