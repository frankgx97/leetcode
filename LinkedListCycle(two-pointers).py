# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''
        fast and slow pointer - ac
        use two pointers
        fast pointer starts at head.next(if head.next == None, return false, cuz there's won't be a loop if head.next is none), move 2 steps per loop, if reach none, return false.
        slow pointer starts at head, move 1 steps per loop. slow pointer is not likely to reach none because it is always behind the fast one.
        once slow and fast pointer meets, return true.
        we can imagine a playground with runway, if two person runs on it with different speed, they will always meet.
        
        '''
        if not head:
            return False
        left = head
        if head.next:
            right = head.next
        else:
            return False
        while right and right.next:
            if left == right:
                return True
            right = right.next.next
            left = left.next
        return False
