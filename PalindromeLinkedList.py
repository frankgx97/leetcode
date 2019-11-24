# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        reverse first half of list - ac
        two pass, O(n) time & O(1) space
        first iterate,get the length of list
        then reverse first half of the list
        '''
        length = 0
        current = head
        while current:
            length+=1
            current = current.next
        
        if length <= 1:
            return True
            
        current = head
        prev = None
        nex = None
        
        current_len = 1
        while current_len <= length//2:
            nex = current.next
            current.next = prev
            prev = current
            current = nex
            current_len += 1
            
        '''
        at this point
        current points to a unreversed node, prev points to a reversed
        ex.
        1 <- 2 <- 3 -> 4 -> 5
             ^    ^
           prev  curr
           
        1 <- 2 -> 3 -> 4
             ^    ^
           prev  curr
        
        '''
        
        
        if length%2 == 1:
            current_left = prev
            current_right = current.next
        else:
            current_left = prev
            current_right = current
                
        while current_left and current_right:
            if current_left.val != current_right.val:
                return False
            current_left = current_left.next
            current_right = current_right.next
        return True
            
            
            
