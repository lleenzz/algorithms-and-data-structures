class Queue:
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
        return self.items.pop(0)

    def __str__(self):
        return str(self.items)

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()
        return "ok"

    def front(self):
        if self.is_empty():
            return "error"
        return self.items[0]

    def exit(self):
        return "bye"

qu = Queue()

while True:
    cmd = input().split()
    req = cmd[0]

    if req == "push":
        print(qu.push(int(cmd[1])))
    elif req == "pop":
        print(qu.pop())
    elif req == "front":
        print(qu.front())
    elif req == "size":
        print(qu.size())
    elif req == "clear":
        print(qu.clear())
    elif req == "exit":
        print(qu.exit())
        break