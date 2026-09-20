def bubble_sort(A):
    for i in range(len(A)-1):
        for j in range(len(A) - i - 1):
            if (A[j][0]**2 + A[j][1]**2) ** (1 / 2) > (A[j+1][0]**2 + A[j+1][1]**2) ** (1 / 2):
                A[j], A[j + 1] = A[j + 1], A[j]
    return A



n = int(input())
points = []


for i in range(n):
    point = list(map(int, input().split()))
    points.append(point)


bubble_sort(points)
for  p in points:
    print(*p)
