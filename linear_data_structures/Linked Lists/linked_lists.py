# ============================================================
#  Data Structures — Linked Lists
#  Singly | Doubly | Circular
# ============================================================


# ── Shared Node for Singly & Circular ──────────────────────
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ── Node for Doubly Linked List ────────────────────────────
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# ══════════════════════════════════════════════════════════
#  1. SINGLY LINKED LIST
# ══════════════════════════════════════════════════════════
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # ── Append (end) ──────────────────────────────────────
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # ── Prepend (beginning) ───────────────────────────────
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # ── Insert after a specific value ─────────────────────
    def insert_after(self, target, data):
        current = self.head
        while current:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next
        print(f"Value {target} not found.")
        return False

    # ── Delete by value ───────────────────────────────────
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    # ── Search ────────────────────────────────────────────
    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    # ── Display ───────────────────────────────────────────
    def display(self):
        current = self.head
        parts = []
        while current:
            parts.append(f"[{current.data}]")
            current = current.next
        print(" -> ".join(parts) + " -> None")

    # ── Length ────────────────────────────────────────────
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # ── Reverse ───────────────────────────────────────────
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


# ══════════════════════════════════════════════════════════
#  2. DOUBLY LINKED LIST
# ══════════════════════════════════════════════════════════
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # ── Append (end) ──────────────────────────────────────
    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    # ── Prepend (beginning) ───────────────────────────────
    def prepend(self, data):
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    # ── Insert after a specific value ─────────────────────
    def insert_after(self, target, data):
        current = self.head
        while current:
            if current.data == target:
                new_node = DoublyNode(data)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return True
            current = current.next
        print(f"Value {target} not found.")
        return False

    # ── Delete by value ───────────────────────────────────
    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return True
            current = current.next
        return False

    # ── Search ────────────────────────────────────────────
    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    # ── Display forward ───────────────────────────────────
    def display_forward(self):
        current = self.head
        parts = []
        while current:
            parts.append(f"[{current.data}]")
            current = current.next
        print(" <-> ".join(parts) + " <-> None")

    # ── Display backward ──────────────────────────────────
    def display_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        parts = []
        while current:
            parts.append(f"[{current.data}]")
            current = current.prev
        print(" <-> ".join(parts) + " <-> None")

    # ── Length ────────────────────────────────────────────
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# ══════════════════════════════════════════════════════════
#  3. CIRCULAR LINKED LIST
# ══════════════════════════════════════════════════════════
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # ── Append (end) ──────────────────────────────────────
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    # ── Prepend (beginning) ───────────────────────────────
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    # ── Delete by value ───────────────────────────────────
    def delete(self, data):
        if not self.head:
            return
        # Deleting head
        if self.head.data == data:
            if self.head.next == self.head:   # only one node
                self.head = None
                return
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return
        # Deleting other nodes
        current = self.head
        while current.next != self.head:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    # ── Search ────────────────────────────────────────────
    def search(self, value):
        if not self.head:
            return -1
        current = self.head
        index = 0
        while True:
            if current.data == value:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break
        return -1

    # ── Display ───────────────────────────────────────────
    def display(self):
        if not self.head:
            print("Empty list")
            return
        current = self.head
        parts = []
        while True:
            parts.append(f"[{current.data}]")
            current = current.next
            if current == self.head:
                break
        print(" -> ".join(parts) + " -> (head)")

    # ── Length ────────────────────────────────────────────
    def length(self):
        if not self.head:
            return 0
        count = 1
        current = self.head.next
        while current != self.head:
            count += 1
            current = current.next
        return count