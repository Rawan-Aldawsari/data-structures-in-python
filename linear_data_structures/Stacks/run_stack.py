# ============================================================
#  main_stack.py  —  Interactive demo for all Stack features
# ============================================================

from stack import StackArray, StackLinkedList, is_balanced, UndoSystem


def separator(title=""):
    print("\n" + "=" * 45)
    if title:
        print(f"  {title}")
        print("=" * 45)


def demo_stack_array():
    separator("Stack using Array")
    s = StackArray()
    for val in [10, 20, 30, 40]:
        s.push(val)
    s.display()
    print(f"\n  peek  → {s.peek()}")
    print(f"  pop   → {s.pop()}")
    print(f"  size  → {s.size()}")
    print()
    s.display()


def demo_stack_linked_list():
    separator("Stack using Linked List")
    s = StackLinkedList()
    for val in ["A", "B", "C", "D"]:
        s.push(val)
    s.display()
    print(f"\n  peek  → {s.peek()}")
    print(f"  pop   → {s.pop()}")
    print(f"  size  → {s.size()}")
    print()
    s.display()


def demo_balanced():
    separator("Balanced Expression Checker")
    test_cases = [
        "(a + b) * (c - d)",
        "((x + y)",
        "{[()]}",
        "{[(])}",
        "",
        "((()))",
    ]
    for expr in test_cases:
        result = "✔ Balanced" if is_balanced(expr) else "✖ Not balanced"
        display = expr if expr else "(empty string)"
        print(f"  {result:18}  →  {display}")


def demo_undo_system():
    separator("Undo / Redo System")
    editor = UndoSystem()
    editor.do("Type 'Hello'")
    editor.do("Bold text")
    editor.do("Change font size")
    print()
    print(editor.undo())
    print(editor.undo())
    print(editor.redo())
    print()
    editor.history()


def menu():
    options = {
        "1": ("Stack using Array",            demo_stack_array),
        "2": ("Stack using Linked List",       demo_stack_linked_list),
        "3": ("Balanced Expression Checker",   demo_balanced),
        "4": ("Undo / Redo System",            demo_undo_system),
        "5": ("Run all demos",                 None),
        "0": ("Exit",                          None),
    }

    while True:
        separator("Stack — Main Menu")
        for key, (label, _) in options.items():
            print(f"  [{key}]  {label}")
        print()

        choice = input("  Choose: ").strip()

        if choice == "0":
            print("\n  Bye! 👋\n")
            break
        elif choice == "5":
            demo_stack_array()
            demo_stack_linked_list()
            demo_balanced()
            demo_undo_system()
        elif choice in options:
            _, func = options[choice]
            func()
        else:
            print("  Invalid choice — try again.")

        input("\n  Press Enter to continue...")


if __name__ == "__main__":
    menu()