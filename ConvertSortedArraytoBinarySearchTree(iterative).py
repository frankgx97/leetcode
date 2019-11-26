# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
        iterative(stack) - ac
        use the mid of the array as root
        left part for the l subtree
        right part for the r subtree
        
        in each iteration, construct a tuple, including
        - subarray
        - current node(will be the parent of next node)
        - direction for the next node(left child or right child)
        '''
        def bst_iterative(arr):
            
            if not arr:
                return None
            
            stack = []
            
            mid = len(arr)//2
            rootval = arr[mid]
            lsub = arr[:mid]
            rsub = arr[mid+1:]
            
            treeroot = TreeNode(rootval)
            
            stack.append((lsub,treeroot,'l'))
            stack.append((rsub,treeroot,'r'))
            
            while stack:
                stacktop = stack.pop(-1)
                curr = stacktop[0]
                prev_node = stacktop[1]
                direction = stacktop[2]
                
                if not curr:
                    continue
                
                mid = len(curr)//2
                rootval = curr[mid]
                lsub = curr[:mid]
                rsub = curr[mid+1:]
                curr_node = TreeNode(rootval)
                if direction == 'r':
                    prev_node.right = curr_node
                else:
                    prev_node.left = curr_node
                stack.append((rsub,curr_node,'r'))
                stack.append((lsub,curr_node,'l'))
            return treeroot
        
        return bst_iterative(nums)
