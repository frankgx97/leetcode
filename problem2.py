# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def assembleList(self,l):
        former = None
        for i in l:
            current = ListNode(i)
            if former == None:
                former = current
                first = current
            else:
                former.next = current
                former = current
        return first
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        flag = False #进位标记
        while True:
            current = l1.val + l2.val
            if flag == True:
                current += 1
            if current >= 10:
                current -= 10
                flag = True
            else:
                flag = False
            result.append(current)
            if l1.next == None and l2.next == None:
                if flag == True:
                    result.append(1)
                break
            if l1.next != None:
                l1 = l1.next
            else:
                l1.val = 0
            if l2.next != None:
                l2 = l2.next
            else:
                l2.val = 0
        print (result)
        return self.assembleList(result)