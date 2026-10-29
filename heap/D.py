import heapq
import sys

heap = []
for line in sys.stdin:
    s = line.split()
    if s[0] == 'ADD':
        heapq.heappush(heap, -int(s[1]))
    elif s[0] == 'EXTRACT':
        if not heap:
            print("CANNOT")
        else:
            print(-heapq.heappop(heap))
    elif s[0] == 'CLEAR':
        heap = []