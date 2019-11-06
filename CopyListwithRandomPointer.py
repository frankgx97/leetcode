"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        '''
        O(2n) extra space, O(n) time - ac
        first init two lists(visited and nodes), in visited list we store the ref of each node in the original lists, in nodes list we store the copy of the each nodes in the original list.
        then iterate both list at the same time, find the index of the node that each node's next and random pointer is pointing to. and set the pointers in nodes in the nodes list to nodes in certain indecies.
        '''
        if head == None:
            return None
        visited = []
        nodes = []
        current = head
        while current:
            curr_new = ListNode(current.val)
            visited.append(current)
            nodes.append(curr_new)
            current = current.next
        
        current = head
        current_new_index = 0
        while current:
            new_next = nodes[visited.index(current.next)] if current.next else None
            new_rand = nodes[visited.index(current.random)] if current.random else None
            
            nodes[current_new_index].next = new_next
            nodes[current_new_index].random = new_rand
            current_new_index += 1
            current = current.next
        return nodes[0]
