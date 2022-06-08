# ----- Node ------
class Node:
  # store your DATA and LEFT and RIGHT values here
  def __init__(self, value):
      self.left = None
      self.right = None
      self.data = value

class Bst:
  def __init__(self):
    self.parent = None
    pass

  def insert(self, value):
    #This is where you will insert a value into the Binary Search Tree
    if self.value:
      if value < self.value:
        if self.left is None:
          self.left = Node(value)
        else:
          self.left.insert(value)
      elif value > self.value:
          if self.right is None:
            self.right = Node(value)
          else:
            self.right.insert(value)
      else:
        self.value = value

  def contains(self, look_value):
    # this is where you'll search the BST and return TRUE or FALSE if the value exists in the BST
    if look_value < self.value:
      if self.left is None:
        return False
      return True
    elif look_value > self.value:
      if self.right is None:
        return False
      else:
        return True
    else:
      return True

  def remove(self, value):
    # this is where you will remove a value from the BST
    pass




