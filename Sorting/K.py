n = int(input())

if n == 1:
    print(1)
else:
    A = [1, 2]

    for i in range(3, n + 1):
        mid = len(A) // 2
        A.append(A[mid])
        A[mid] = i

    print(*A)