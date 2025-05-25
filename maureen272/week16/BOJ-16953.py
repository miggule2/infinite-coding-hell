# BOJ-16953- A → B
def min_operations(A, B):
    operations = 0
    while B > A:
        if B % 2 == 0:
            B //= 2
        elif B % 10 == 1:
            B //= 10
        else:
            return -1
        operations += 1
    return operations + 1 if B == A else -1

A, B = map(int, input().split())

print(min_operations(A, B))