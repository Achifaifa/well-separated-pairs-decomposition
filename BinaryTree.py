class BinaryTree():
  """
  Class BinaryTree for the Well Separated Decomposition
  """
  
  def __init__(self,val):

    self.value = val
    self.left = None
    self.right = None
    self.parent = None
  
  def __repr__(self):

    return str(self.inorder())

  def set_left(self,node):

    self.left=BinaryTree(node) if not isinstance(node, BinaryTree) else node
    self.left.parent = self

  def set_right(self,node):

    self.right = BinaryTree(node) if not isinstance(node, BinaryTree) else node
    self.right.parent = self

  def inorder(self):
 
    left  = self.left.inorder()  if self.left  is not None else left  = []
    right = self.right.inorder() if self.right is not None else right = []                      
    return filter(None,[left,[self.value],right]) 