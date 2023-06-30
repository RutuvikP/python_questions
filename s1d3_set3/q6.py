from queue import Queue

class Stack:
    def __init__(self):
        self.queue = Queue()

    def push(self, item):
        # Move all existing elements to the temporary queue
        temp_queue = Queue()
        while not self.queue.empty():
            temp_queue.put(self.queue.get())

        # Add the new item to the temporary queue
        self.queue.put(item)

        # Move the elements back from the temporary queue to the main queue
        while not temp_queue.empty():
            self.queue.put(temp_queue.get())

    def pop(self):
        if not self.is_empty():
            return self.queue.get()
        else:
            print("None")
            return None

    def is_empty(self):
        return self.queue.empty()

    def size(self):
        return self.queue.qsize()

    def top(self):
        if not self.is_empty():
            top_item = self.queue.get()
            self.queue.put(top_item)  # Re-insert the item at the top of the queue
            return top_item
        else:
            print("None")
            return None

stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)