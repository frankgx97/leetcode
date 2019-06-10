# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        la = self.getLength(headA)
        lb = self.getLength(headB)
        print(la,lb)
        if la > lb:
            headA = self.move(headA, la-lb)
        else:
            headB = self.move(headB, lb-la)

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
            
            
    def move(self, head, steps):
        for i in range(steps):
            head = head.next
        return head
        
    def getLength(self, head):
        l = 0
        while head != None:
            l += 1
            head = head.next
        return l
