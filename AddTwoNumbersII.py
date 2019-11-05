# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
iterate through each linked list and read them to stack.
pop two stacks at the same time and calculate the answer, and store it in the result stack
be aware of a corner case that there may be a carry at the end of addition.
pop the result stack and construct the result linked list
'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        carry = 0
        result = []
        while len(stack1) > 0 or len(stack2) > 0:
            curr = 0
            if len(stack1) > 0:
                curr += stack1[-1]
                stack1.pop(-1)
            if len(stack2) > 0:
                curr += stack2[-1]
                stack2.pop(-1)
            curr += carry
            carry = 0
            if curr >= 10:
                curr -= 10
                carry = 1
            result.append(curr)
        if carry == 1:
            result.append(1)
        dummy = ListNode(-1)
        current = dummy
        while len(result) > 0:
            current_node = ListNode(result[-1])
            result.pop(-1)
            current.next = current_node
            current = current.next
        return dummy.next
