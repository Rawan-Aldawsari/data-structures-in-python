from arrays import StaticArray, DynamicArray, MultiDimensionalArray


def demo_static():
    print("\nStatic Array (size=5)")
    arr = StaticArray(5)
    arr.set(0, 10)
    arr.set(2, 30)
    arr.set(4, 50)
    arr.display()
    print("get(2) ->", arr.get(2))
    print("search(30) -> index", arr.search(30))


def demo_dynamic():
    print("\nDynamic Array")
    arr = DynamicArray()
    for v in [5, 10, 15, 20]:
        arr.append(v)
    arr.display()

    arr.insert(2, 99)
    print("After insert(2, 99):")
    arr.display()

    arr.remove(10)
    print("After remove(10):")
    arr.display()

    print("search(99) -> index", arr.search(99))
    print("pop() ->", arr.pop())
    arr.display()


def demo_matrix():
    print("\n2D Matrix (3x3)")
    mat = MultiDimensionalArray(3, 3)
    mat.set(0, 0, 1)
    mat.set(1, 1, 5)
    mat.set(2, 2, 9)
    mat.display()
    print("get(1,1) ->", mat.get(1, 1))
    print("search(9) -> position", mat.search(9))


def menu():
    options = {
        "1": ("Static Array", demo_static),
        "2": ("Dynamic Array", demo_dynamic),
        "3": ("2D Matrix", demo_matrix),
        "4": ("Run all demos", lambda: [f() for f in [demo_static, demo_dynamic, demo_matrix]]),
    }

    print("\n==============================")
    print("   Arrays Data Structures")
    print("==============================")
    for k, (name, _) in options.items():
        print(f"{k}. {name}")
    print("0. Exit")

    while True:
        choice = input("\nChoose > ").strip()
        if choice == "0":
            break
        elif choice in options:
            options[choice][1]()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()