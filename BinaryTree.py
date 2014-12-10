"""Class BinaryTree for the Well Separated Decomposition"""



class BinaryTree():
    def __init__(self,val):
        self._value = val
        self._left = None
        self._right = None
        self._parent = None
    
    def __repr__(self):
        return str(self.inorder())


    def set_left(self,node):
        self._left = node
        if not isinstance(node, BinaryTree):
            self._left = BinaryTree(node)
        self._left._parent = self

    def set_right(self,node):
        self._right = node
        if not isinstance(node, BinaryTree):
            self._right = BinaryTree(node)
        self._right._parent = self

    def inorder(self):
        if self._left is not None:
            left = self._left.inorder()
        else:
            left = []
        if self._right is not None:
            right = self._right.inorder()
        else:
            right = []
        return filter(None,[left,[self._value],right]) 

    def right(self):
        return self._right

    def left(self):
        return self._left

    def parent(self):
        return self._parent
