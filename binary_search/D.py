def f(a,b,c,d, x):
    return a*x**3+b*x**2+c*x+d

def binary_search():
    l, r = -10**10, 10**10
    for i in range(1000):
        m = (l+r)/2
        if f(a, b, c, d, m) * f(a, b, c, d, l) > 0:
            l = m
        else:
            r = m
    return l



arr = list(map(int, input().split()))
a, b, c, d = arr[0], arr[1], arr[2], arr[3]

ans = binary_search()

print(f"{ans:.10f}")