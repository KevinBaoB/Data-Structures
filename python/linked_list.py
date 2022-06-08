# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, head, length):
    self.head_node = Node(head)
    self.node_length = length

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def remove(self, node_to_remove):
    # write your code to REMOVE an element from the Linked List
    current_node = self.head_node
    if current_node == node_to_remove:
      self.head_node = current_node.next_node
    else:
      while current_node:
        next_node = current_node.next_node
        if next_node == node_to_remove:
          current_node.next_node = next_node.next_node
          current_node = None
        else:
          current_node = next_node

  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    
      



