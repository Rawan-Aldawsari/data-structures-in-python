class StaticArray:
    def __init__(self, size: int):
        self.size = size
        self.data = [None] * size

    def set(self, index: int, value) -> None:
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError(f"Index {index} out of range (size={self.size})")

    def get(self, index: int):
        if 0 <= index < self.size:
            return self.data[index]
        raise IndexError(f"Index {index} out of range (size={self.size})")

    def search(self, value) -> int:
        for i, v in enumerate(self.data):
            if v == value:
                return i
        return -1

    def update(self, index: int, value) -> None:
        self.set(index, value)

    def display(self) -> None:
        print("Index:", list(range(self.size)))
        print("Value:", self.data)


class DynamicArray:
    def __init__(self):
        self.data = []

    def append(self, value) -> None:
        self.data.append(value)

    def insert(self, index: int, value) -> None:
        self.data.insert(index, value)

    def remove(self, value) -> bool:
        if value in self.data:
            self.data.remove(value)
            return True
        return False

    def pop(self, index: int = -1):
        if not self.data:
            raise IndexError("Pop from empty array")
        return self.data.pop(index)

    def get(self, index: int):
        return self.data[index]

    def update(self, index: int, value) -> None:
        self.data[index] = value

    def search(self, value) -> int:
        for i, v in enumerate(self.data):
            if v == value:
                return i
        return -1

    def length(self) -> int:
        return len(self.data)

    def display(self) -> None:
        print(f"DynamicArray (len={len(self.data)}):", self.data)


class MultiDimensionalArray:
    def __init__(self, rows: int, cols: int, default=0):
        self.rows = rows
        self.cols = cols
        self.data = [[default for _ in range(cols)] for _ in range(rows)]

    def set(self, row: int, col: int, value) -> None:
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise IndexError(f"({row},{col}) out of bounds ({self.rows}x{self.cols})")

    def get(self, row: int, col: int):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        raise IndexError(f"({row},{col}) out of bounds ({self.rows}x{self.cols})")

    def search(self, value) -> tuple:
        for r, row in enumerate(self.data):
            for c, v in enumerate(row):
                if v == value:
                    return (r, c)
        return (-1, -1)

    def fill(self, value) -> None:
        for r in range(self.rows):
            for c in range(self.cols):
                self.data[r][c] = value

    def display(self) -> None:
        print(f"Matrix {self.rows}x{self.cols}:")
        col_labels = "     " + "  ".join(f"[{c}]" for c in range(self.cols))
        print(col_labels)
        for i, row in enumerate(self.data):
            formatted = "  ".join(str(v).rjust(3) for v in row)
            print(f"[{i}]  {formatted}")