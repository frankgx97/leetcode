# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        current = head
        prev = dummy
        while current and current.next:
            print(current.val)
            if current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    print('==',current.val)
                    current.next = current.next.next
                prev.next = current.next
                current = prev.next
            else:
                current = current.next
                prev = prev.next
        return dummy.next
