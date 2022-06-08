class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
  def __init__(self, stack_arr):
      self.stack_arr = stack_arr
      self.stack_length = len(stack_arr)

  def push(self, data):
    # write your code to add data following LIFO and return the Stack
    self.stack_arr.append(data)
    return self.stack_arr

  def pop(self):
    # write your code to removes the data following LIFO and return the Stack
    self.stack_arr.pop()
    return self.stack_arr

  def size(self):
    # write your code that returns the size of the Stack
    return self.stack_length
