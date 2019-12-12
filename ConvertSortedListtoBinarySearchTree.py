# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        '''
        use fast-slow pointers to find the mid of the list as root
        left part for the l subtree
        right part for the r subtree
        '''
        root = None
        def trav(parent,direc,head):
            nonlocal root
            prev = None
            slow = head
            fast = head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            curr = TreeNode(slow.val)
            if parent:
                if direc == 'l':
                    parent.left = curr
                elif direc == 'r':
                    parent.right = curr
            else:
                root = curr

            if prev and prev.next:
                prev.next = None
                trav(curr,'l',head)
            if slow and slow.next:
                trav(curr,'r',slow.next)
            return
        if not head:
            return None
        trav(None,'',head)
        return root
