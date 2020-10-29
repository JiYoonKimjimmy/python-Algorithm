class SparseArray:
    def __init__(self, arr, size):
        self.arr = arr
        self.size = size

    def set(self, i, val):
        self.arr[i] = val

    def get(self, i):
        return self.arr[i]


size = 5
arr = [0] * size

sparseArray = SparseArray(arr, size)
sparseArray.set(1, 1)
print(sparseArray.get(1))
