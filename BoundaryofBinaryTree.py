# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        '''
        calculate left bound, right bound and leaf respectively - ac
        first use iteration to traverse left bound of the tree: start from the left of root, if left exist go left, else go right, until reach leaf(include root, do not include leaf)
        then traverse recursively from root to record all leaf nodes(no matter which order),do not include root if root is a leaf node(in case of root is the only node in the tree, including root here will lead to duplication with the list of left bound)
        then use iteration to traverse right bound of the tree: start from right of root, if right exist go right, else go left, until reach leaf(do not include root and leaf)
        finally, concatente left bound, leaf and right bound.
        '''
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def is_leaf(node):
            if not node.left and not node.right:
                return True
            else:
                return False
            
        def left_bound(root):
            r = [root.val]
            if not root.left:
                return r
            else:
                current = root.left
            while current:
                if not is_leaf(current):
                    r.append(current.val)
                    if current.left:
                        current = current.left
                    else:
                        current = current.right
                else:
                    break
            return r
        
        def right_bound(root):
            r = []
            if not root.right:
                return r
            else:
                current = root.right
            while current:
                if current == root:
                    current = current.right
                elif not is_leaf(current):
                    r.append(current.val)
                    if current.right:
                        current = current.right
                    else:
                        current = current.left
                else:
                    break
            return r
        

        def leaf(root,root_of_tree):
            if not root:
                return
            if is_leaf(root) and root != root_of_tree:
                leaves.append(root.val)
            leaf(root.left,root)
            leaf(root.right,root)
            return
        
        if not root:
            return []
        leaves = []
        leaf(root,root)
        
        return left_bound(root)+ leaves + right_bound(root)[::-1]
