# ============================================================
#  stack.py  —  Stack implementations + practical examples
# ============================================================


# ─────────────────────────────────────────
#  1. Stack using Array (List)
# ─────────────────────────────────────────

class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack (top → bottom):")
        for item in reversed(self.stack):
            print(f"  | {item:^10} |")
        print("  " + "-" * 14)


# ─────────────────────────────────────────
#  2. Stack using Linked List
# ─────────────────────────────────────────

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if not self.top:
            return "Stack is empty"
        removed = self.top.data
        self.top = self.top.next
        self._size -= 1
        return removed

    def peek(self):
        if self.top:
            return self.top.data
        return "Stack is empty"

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack (top → bottom):")
        current = self.top
        while current:
            print(f"  | {current.data:^10} |")
            current = current.next
        print("  " + "-" * 14)


# ─────────────────────────────────────────
#  3. Balanced Parentheses Checker
# ─────────────────────────────────────────

def is_balanced(expression):
    """
    Checks if parentheses, brackets, and braces are balanced.
    Examples:
        "(a + b) * (c - d)"  →  True
        "((x + y)"           →  False
        "{[()]}"             →  True
    """
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    opening = set('([{')

    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in matching:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()

    return len(stack) == 0


# ─────────────────────────────────────────
#  4. Undo / Redo System
# ─────────────────────────────────────────

class UndoSystem:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def do(self, action):
        """Perform an action and save it to undo history."""
        self._undo_stack.append(action)
        self._redo_stack.clear()          # new action clears redo history
        print(f"  ✔  Did: {action}")

    def undo(self):
        if self._undo_stack:
            action = self._undo_stack.pop()
            self._redo_stack.append(action)
            return f"  ↩  Undo: {action}"
        return "  ✖  Nothing to undo"

    def redo(self):
        if self._redo_stack:
            action = self._redo_stack.pop()
            self._undo_stack.append(action)
            return f"  ↪  Redo: {action}"
        return "  ✖  Nothing to redo"

    def history(self):
        print("  Undo stack:", self._undo_stack)
        print("  Redo stack:", self._redo_stack)