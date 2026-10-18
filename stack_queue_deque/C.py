s = input().split()
stack = []

for el in s:
    if not el.isnumeric():
        b = stack.pop()
        a = stack.pop()
        res = 0
        if el == "*":
            res = a * b
        if el == "+":
            res = a + b
        if el == "-":
            res = a - b
        if el == "/":
            res = a / b
        stack.append(res)
    else:
        stack.append(int(el))
print(stack[0])