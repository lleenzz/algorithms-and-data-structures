data = list(map(int, input().split()))
a = data[1:]
stack = []
count = 0

for el in a:
    if stack and stack[-1][0] == el:
        stack[-1][1] += 1
    else:
        while stack and stack[-1][1] >= 3:
            count += stack.pop()[1]
        if stack and stack[-1][0] == el:
            stack[-1][1] += 1
        else:
            stack.append([el, 1])

while stack and stack[-1][1] >= 3:
    count += stack.pop()[1]

print(count)