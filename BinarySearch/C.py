def f(x):
    return x**2 + x**(1/2)

def binary_search(x):
    l, r = 1, 10**10
    for i in range(1000):
        m = (l+r)/2
        if f(m) <= x:
            l = m
        else:
            r = m
    return l


c = float(input())

print(binary_search( c))