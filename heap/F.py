import heapq

n = int(input())
arr = []
for _ in range(n):
    t, l = map(int, input().split())
    arr.append((t,l))

arr.sort()
heap = []
count = 0

for t, l in arr:
    while heap and heap[0] <= t:
        heapq.heappop(heap)
    heapq.heappush(heap, t + l)

    if len(heap) > count:
        count = len(heap)

print(count)