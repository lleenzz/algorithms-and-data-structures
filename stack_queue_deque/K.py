n = int(input())
a = list(map(int, input().split()))

stack = []
pref = [0]

for x in a:
    pref.append(pref[-1] + x)

best = 0
best_l = best_r = 1

for i in range(n):
    left = i + 1

    while stack and stack[-1][0] > a[i]:
        value, left = stack.pop()
        summa = pref[i] - pref[left - 1]
        price = summa * value

        if price > best:
            best = price
            best_l = left
            best_r = i

    stack.append((a[i], left))

while stack:
    value, left = stack.pop()
    summa = pref[n] - pref[left - 1]
    price = summa * value

    if price > best:
        best = price
        best_l = left
        best_r = n

print(best)
print(best_l, best_r)