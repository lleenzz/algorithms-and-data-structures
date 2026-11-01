import heapq

n = int(input())
arr = []
for _ in range(n):
    el = int(input())
    arr.append(el)

heap = []

for i in range(n):
    fish = arr[i]
    t = max(1000 - fish, 1)
    heapq.heappush(heap, (t, i, fish))

cur_t = 0
cur_pos = 0
while heap:
    t, pos, fish = heapq.heappop(heap)
    run_t = abs(pos - cur_pos)
    need_t = run_t + cur_t
    if need_t > t:
        print(t)
        break

    cur_t = t
    cur_pos = pos
    fish += 1

    next_t = cur_t + max(1000 - fish, 1)
    heapq.heappush(heap, (next_t, pos, fish))

