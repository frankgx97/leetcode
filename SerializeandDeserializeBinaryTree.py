# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
    recursive pre order traversal - ac
    '''

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        path = ''
        def ser(root):
            nonlocal path
            if not root:
                path += '#,'
                return 
            else:
                path += str(root.val)+','
                ser(root.left)
                ser(root.right)
        ser(root)
        return path[:-1]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def des(data):
            if not data or data[0] == '#':
                data.pop(0)
                return None
            curr = TreeNode(data[0])
            #print(data,curr)
            data.pop(0)
            curr.left = des(data)
            curr.right = des(data)
            return curr
        data = data.split(',')
        h = des(data)
        return h
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
