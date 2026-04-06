# generate code for queue and its operations
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print("Front item",queue.peek())  # Output: 1
print("Dequeue item:", queue.dequeue())  # Output: 1
print("Front item after dequeue:",queue.peek())  # Output: 2
print("Queue size after dequeue:", queue.size())  # Output: 1
print("Dequeue item:", queue.dequeue())  # Output: 2
print("Queue size after dequeue:", queue.size())


