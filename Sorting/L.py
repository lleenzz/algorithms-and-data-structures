def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort_2(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


A = list(map(int, input().split()))
B = list(map(int, input().split()))

bubble_sort(A)
bubble_sort_2(B)

c = 0
for i in range(len(A)):
    c += A[i] * B[i]

print(c)

