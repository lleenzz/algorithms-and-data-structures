import sys
A = []

for line in sys.stdin:
    A.append(line.strip())



B = []

while len(A) > 0:
    m_i = 0

    for j in range(1, len(A)):
        if A[j] + A[m_i] > A[m_i] + A[j]:
            m_i = j

    B.append(A[m_i])
    A.pop(m_i)

print("".join(B))


