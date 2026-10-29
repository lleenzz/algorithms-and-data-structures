import heapq

n = int(input())
arr = list(map(int, input().split()))

heapq.heapify(arr)

cost = 0
while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    s = a + b
    cost += s*0.05
    heapq.heappush(arr, s)

print(cost)