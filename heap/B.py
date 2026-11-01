class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.shiftUp(self.size)

    def shiftUp(self, i):
        while i // 2 > 0 and self.heap[i] < self.heap[i // 2]:
            self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i //= 2

    def extractMin(self):
        if self.size == 0:
            return None
        removed = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.shiftDown(1)
        return removed

    def shiftDown(self, i):
        while i * 2 <= self.size:
            j = self.indMinChild(i)
            if self.heap[i] > self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def indMinChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap[i * 2] > self.heap[i * 2 + 1]:
            return i * 2 + 1
        return i * 2


n = int(input())
arr = list(map(int, input().split()))
heap = MinHeap()

for x in arr:
    heap.insert(x)

sorted_arr = []

for _ in range(n):
    sorted_arr.append(heap.extractMin())

print(*sorted_arr)