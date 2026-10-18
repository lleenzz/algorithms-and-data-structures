s = input()
stack = []
ans = True

for el in s:
    if el in ["(", "[", "{"]:
        stack.append(el)
        continue
    if len(stack) != 0 and (el == ")" and stack[-1] == "(" or el == "]" and stack[-1] == "[" or el == "}" and stack[-1] == "{"):
        stack.pop()
    else:
        ans = False
        break

if len(stack) != 0:
    ans = False

print("yes" if ans else "no")