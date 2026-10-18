class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        return "ok"

    def pop(self):
        if self.is_empty():
            return "error"
        return self.items.pop()

    def __str__(self):
        return str(self.items)

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()
        return "ok"

    def back(self):
        if self.is_empty():
            return "error"
        return self.items[-1]

    def exit(self):
        return "bye"

s = Stack()

while True:
    cmd = input().split()
    req = cmd[0]

    if req == "push":
        print(s.push(int(cmd[1])))
    elif req == "pop":
        print(s.pop())
    elif req == "back":
        print(s.back())
    elif req == "size":
        print(s.size())
    elif req == "clear":
        print(s.clear())
    elif req == "exit":
        print(s.exit())
        break