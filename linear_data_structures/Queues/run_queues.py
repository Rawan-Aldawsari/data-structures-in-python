from queues import SimpleQueue, CircularQueue, PriorityQueue, Deque


def hospital_simulation():
    print("\n--- Hospital Queue Simulation ---")
    q = SimpleQueue()
    q.enqueue("Patient 1")
    q.enqueue("Patient 2")
    q.enqueue("Patient 3")
    q.display()
    print("Serving:", q.dequeue())
    q.display()


def menu():
    print("\n" + "="*40)
    print("       QUEUE DATA STRUCTURES")
    print("="*40)
    print("1. Simple Queue   (FIFO)")
    print("2. Circular Queue (Fixed Size)")
    print("3. Priority Queue (By Priority)")
    print("4. Deque          (Double-Ended)")
    print("5. Hospital Simulation")
    print("0. Exit")
    print("="*40)

    choice = input("Choose: ").strip()

    if choice == "1":
        print("\n--- Simple Queue ---")
        q = SimpleQueue()
        q.enqueue(10)
        q.enqueue(20)
        q.enqueue(30)
        q.display()
        print("Peek:", q.peek())
        print("Dequeue:", q.dequeue())
        q.display()

    elif choice == "2":
        print("\n--- Circular Queue (size=4) ---")
        q = CircularQueue(4)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.display()
        print("Dequeue:", q.dequeue())
        q.enqueue(4)
        q.display()

    elif choice == "3":
        print("\n--- Priority Queue ---")
        q = PriorityQueue()
        q.enqueue("Task A", 2)
        q.enqueue("Task B", 1)
        q.enqueue("Task C", 3)
        q.display()
        print("Dequeue:", q.dequeue())
        q.display()

    elif choice == "4":
        print("\n--- Deque ---")
        d = Deque()
        d.add_front(10)
        d.add_rear(20)
        d.add_front(5)
        d.add_rear(25)
        d.display()
        print("Remove Front:", d.remove_front())
        print("Remove Rear:", d.remove_rear())
        d.display()

    elif choice == "5":
        hospital_simulation()

    elif choice == "0":
        print("Goodbye!")
        return

    else:
        print("Invalid choice!")

    again = input("\nBack to menu? (y/n): ").strip().lower()
    if again == "y":
        menu()


menu()