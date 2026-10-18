class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push_back(self, item):
        self.items.append(item)
        return "ok"

    def push_front(self, item):
        self.items = [item] + self.items
        return "ok"

    def pop_front(self):
        if self.is_empty():
            return "error"
        return self.items.pop(0)

    def pop_back(self):
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

    def front(self):
        if self.is_empty():
            return "error"
        return self.items[0]

    def back(self):
        if self.is_empty():
            return "error"
        return self.items[-1]

    def exit(self):
        return "bye"

dq = Deque()

while True:
    cmd = input().split()
    req = cmd[0]

    if req == "push_back":
        print(dq.push_back(int(cmd[1])))
    elif req == "push_front":
        print(dq.push_front(int(cmd[1])))
    elif req == "pop_front":
        print(dq.pop_front())
    elif req == "pop_back":
        print(dq.pop_back())
    elif req == "front":
        print(dq.front())
    elif req == "back":
        print(dq.back())
    elif req == "size":
        print(dq.size())
    elif req == "clear":
        print(dq.clear())
    elif req == "exit":
        print(dq.exit())
        break