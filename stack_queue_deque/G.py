n = map(int, input().split())
a = list(map(int, input().split()))

stack = []
current = 1

for el in a:
    stack.append(el)
    while stack and stack[-1] == current:
        stack.pop()
        current += 1

if stack:
    print("NO")
else:
    print("YES")

