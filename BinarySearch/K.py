def balls(p, time):
    t, z, y = p[0], p[1], p[2]
    cycle = t * z + y
    cycles = time // cycle
    count = cycles * z
    ost_t = time % cycle
    ost_balls = min(z, ost_t // t)
    return count + ost_balls

def good(people, time, M):
    s = 0
    for p in people:
        s += balls(p, time)
    return s >= M

M, N = map(int, input().split())

people = []
for _ in range(N):
    t, z, y = map(int, input().split())
    people.append((t, z, y))

l = -1
r = 10**9

while r - l > 1:
    m = (l + r) // 2
    if good(people, m, M):
        r = m
    else:
        l = m

print(r)


p_balls = []
rem_M = M

for p in people:
    max_can = balls(p, r)
    inflat = min(max_can, rem_M)
    p_balls.append(inflat)
    rem_M -= inflat

print(*p_balls)