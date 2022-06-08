from collections import deque

class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
  def __init__(self, queue_arr):
    self.queue_arr = deque(queue_arr)
    self.queue_length = len(queue_arr)

  def get_queue(self):
    return self.queue_arr

  def enqueue(self, data):
    # write your code to add data to the Queue following FIFO and return the Queue
    self.queue_arr.append(data)
    return self.queue_arr

  def dequeue(self):
    # write your code to removes the data to the Queue following FIFO and return the Queue
    self.queue_arr.popleft()
    return self.queue_arr

  def size(self):
    # write your code that returns the size of the Queue
    return self.queue_length

queue = Queue(["Ram", "Tarun", "Asif", "John"])
print(queue.get_queue())
print(queue.enqueue("Akbar"))
print(queue.dequeue())