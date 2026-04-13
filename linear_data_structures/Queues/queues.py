class SimpleQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Front -> ", end="")
        for item in self.queue:
            print(f"[{item}]", end=" ")
        print("<- Rear")


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            return "Queue is empty"

        value = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return value

    def display(self):
        if self.front == -1:
            print("Empty")
            return

        print("Front -> ", end="")
        i = self.front
        while True:
            print(f"[{self.queue[i]}]", end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print("<- Rear")


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value, priority):
        self.queue.append((priority, value))
        self.queue.sort()

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)[1]
        return "Queue is empty"

    def display(self):
        print("Priority Queue (priority, value):")
        for item in self.queue:
            print(f"  Priority {item[0]} -> [{item[1]}]")


class Deque:
    def __init__(self):
        self.queue = []

    def add_front(self, value):
        self.queue.insert(0, value)

    def add_rear(self, value):
        self.queue.append(value)

    def remove_front(self):
        if self.queue:
            return self.queue.pop(0)
        return "Deque is empty"

    def remove_rear(self):
        if self.queue:
            return self.queue.pop()
        return "Deque is empty"

    def display(self):
        print("Front -> ", end="")
        for item in self.queue:
            print(f"[{item}]", end=" ")
        print("<- Rear")