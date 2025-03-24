def find_path_counts(a, b):
    left, right = 0, 0

    while (a, b) != (1, 1):
        if a > b:
            # 왼쪽 자식에서 올라온 경우
            moves = (a - 1) // b
            left += moves
            a -= moves * b
        else:
            # 오른쪽 자식에서 올라온 경우
            moves = (b - 1) // a
            right += moves
            b -= moves * a

    return left, right

# 입력
A, B = map(int, input().split())
L, R = find_path_counts(A, B)

# 출력
print(L, R)
