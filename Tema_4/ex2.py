class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage of the Queue class:
queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)

print("Queue:", queue.items)  # Output: Queue: [1, 2, 3]

print("Pop:", queue.pop())  # Output: Pop: 1

print("Peek:", queue.peek())  # Output: Peek: 2

print("Is Empty:", queue.is_empty())  # Output: Is Empty: False

print("Size:", queue.size())  # Output: Size: 2
