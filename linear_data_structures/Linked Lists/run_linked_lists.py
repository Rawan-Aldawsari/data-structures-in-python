# ============================================================
#  main_linked_list.py  —  Interactive CLI Simulator
# ============================================================

from linked_lists import SinglyLinkedList, DoublyLinkedList, CircularLinkedList


def run_singly():
    ll = SinglyLinkedList()
    print("\n── Singly Linked List ──────────────────")
    while True:
        print("\n  1. append     2. prepend    3. insert_after")
        print("  4. delete     5. search     6. display")
        print("  7. reverse    8. length     0. back")
        choice = input("  > ").strip()

        if choice == "1":
            v = input("  value: ").strip()
            ll.append(int(v) if v.lstrip('-').isdigit() else v)
            ll.display()
        elif choice == "2":
            v = input("  value: ").strip()
            ll.prepend(int(v) if v.lstrip('-').isdigit() else v)
            ll.display()
        elif choice == "3":
            t = input("  insert after (value): ").strip()
            v = input("  new value: ").strip()
            target = int(t) if t.lstrip('-').isdigit() else t
            new    = int(v) if v.lstrip('-').isdigit() else v
            ll.insert_after(target, new)
            ll.display()
        elif choice == "4":
            v = input("  delete value: ").strip()
            ll.delete(int(v) if v.lstrip('-').isdigit() else v)
            ll.display()
        elif choice == "5":
            v = input("  search value: ").strip()
            idx = ll.search(int(v) if v.lstrip('-').isdigit() else v)
            if idx >= 0:
                print(f"  ✅ found at index {idx}")
            else:
                print("  ❌ not found")
        elif choice == "6":
            ll.display()
        elif choice == "7":
            ll.reverse()
            print("  ↩ reversed:")
            ll.display()
        elif choice == "8":
            print(f"  length = {ll.length()}")
        elif choice == "0":
            break


def run_doubly():
    ll = DoublyLinkedList()
    print("\n── Doubly Linked List ──────────────────")
    while True:
        print("\n  1. append     2. prepend    3. insert_after")
        print("  4. delete     5. search     6. forward")
        print("  7. backward   8. length     0. back")
        choice = input("  > ").strip()

        if choice == "1":
            v = input("  value: ").strip()
            ll.append(int(v) if v.lstrip('-').isdigit() else v)
            ll.display_forward()
        elif choice == "2":
            v = input("  value: ").strip()
            ll.prepend(int(v) if v.lstrip('-').isdigit() else v)
            ll.display_forward()
        elif choice == "3":
            t = input("  insert after (value): ").strip()
            v = input("  new value: ").strip()
            target = int(t) if t.lstrip('-').isdigit() else t
            new    = int(v) if v.lstrip('-').isdigit() else v
            ll.insert_after(target, new)
            ll.display_forward()
        elif choice == "4":
            v = input("  delete value: ").strip()
            ll.delete(int(v) if v.lstrip('-').isdigit() else v)
            ll.display_forward()
        elif choice == "5":
            v = input("  search value: ").strip()
            idx = ll.search(int(v) if v.lstrip('-').isdigit() else v)
            if idx >= 0:
                print(f"  ✅ found at index {idx}")
            else:
                print("  ❌ not found")
        elif choice == "6":
            ll.display_forward()
        elif choice == "7":
            ll.display_backward()
        elif choice == "8":
            print(f"  length = {ll.length()}")
        elif choice == "0":
            break


def run_circular():
    ll = CircularLinkedList()
    print("\n── Circular Linked List ────────────────")
    while True:
        print("\n  1. append     2. prepend    3. delete")
        print("  4. search     5. display    6. length")
        print("  0. back")
        choice = input("  > ").strip()

        if choice == "1":
            v = input("  value: ").strip()
            ll.append(int(v) if v.lstrip('-').isdigit() else v)
            ll.display()
        elif choice == "2":
            v = input("  value: ").strip()
            ll.prepend(int(v) if v.lstrip('-').isdigit() else v)
            ll.display()
        elif choice == "3":
            v = input("  delete value: ").strip()
            ll.delete(int(v) if v.lstrip('-').isdigit() else v)
            ll.display()
        elif choice == "4":
            v = input("  search value: ").strip()
            idx = ll.search(int(v) if v.lstrip('-').isdigit() else v)
            if idx >= 0:
                print(f"  ✅ found at index {idx}")
            else:
                print("  ❌ not found")
        elif choice == "5":
            ll.display()
        elif choice == "6":
            print(f"  length = {ll.length()}")
        elif choice == "0":
            break


def main():
    print("=" * 44)
    print("   🔗 Linked List Interactive Simulator")
    print("=" * 44)
    while True:
        print("\n  1. Singly Linked List")
        print("  2. Doubly Linked List")
        print("  3. Circular Linked List")
        print("  0. Exit")
        choice = input("\n  Choose: ").strip()
        if choice == "1":
            run_singly()
        elif choice == "2":
            run_doubly()
        elif choice == "3":
            run_circular()
        elif choice == "0":
            print("\n  bye! 👋\n")
            break


if __name__ == "__main__":
    main()