class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        if len(items) > limit:
            raise ValueError("Initial stack exceeds limit")
        self.items = items[:limit]
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise OverflowError("Stack is full")

    def pop(self):
        return self.items.pop() if not self.isEmpty() else None  # Return None instead of raising an error

    def peek(self):
        return self.items[-1] if not self.isEmpty() else None

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        try:
            return len(self.items) - self.items.index(target) - 1  # Corrected index calculation
        except ValueError:
            return -1
