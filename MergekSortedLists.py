# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(-1)
        current = dummy
        
        while len(lists) != 0:
            min_index = 0
            min_value = 99999999999
            flg = False
            for i,v in enumerate(lists):
                if v == None:
                    lists.pop(i)
                    flg = True
                    continue
                if v.val < min_value:
                    min_index = i
                    min_value = v.val
            if flg:
                continue
            current.next = lists[min_index]
            current = current.next
            if lists[min_index].next == None:
                lists.pop(min_index)
            else:
                lists[min_index] = lists[min_index].next
        return dummy.next
