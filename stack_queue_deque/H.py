import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

left = deque()
right = deque()

for i in range(n):
    cmd = input().split()
    req = cmd[0]
    if req == "+":
        right.append(int(cmd[1]))
    if req == "*":
        right.appendleft(int(cmd[1]))
    if req == "-":
        print(left.popleft())
    if len(right) > len(left):
        left.append(right.popleft())