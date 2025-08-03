import sys
input = sys.stdin.readline

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def build_hull(points):
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
            upper.pop()
        upper.append(p)
    # 끝점 중복 제거
    return lower[:-1] + upper[:-1]

def on_segment(a, b, p):
    if cross(a, b, p) != 0:
        return False
    return min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])

def point_in_convex(hull, p):
    n = len(hull)
    if n == 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return on_segment(hull[0], hull[1], p)
    # hull은 CCW 순서라고 가정 (monotonic chain으로 생성됨)
    if cross(hull[0], hull[1], p) < 0:
        return False
    if cross(hull[0], hull[-1], p) > 0:
        return False
    # sector 이진 탐색
    lo, hi = 1, n - 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if cross(hull[0], hull[mid], p) >= 0:
            lo = mid
        else:
            hi = mid
    # 삼각형 hull[0], hull[lo], hull[lo+1] 내부/경계 검사
    return cross(hull[lo], hull[lo+1], p) >= 0

def count_captured(own_points, opponent_points):
    hull = build_hull(own_points)
    cnt = 0
    for p in opponent_points:
        if point_in_convex(hull, p):
            cnt += 1
    return cnt

def main():
    N = int(input().strip())
    A = [tuple(map(int, input().split())) for _ in range(N)]
    B = [tuple(map(int, input().split())) for _ in range(N)]
    scoreA = count_captured(A, B)
    scoreB = count_captured(B, A)
    print(f"{scoreA} {scoreB}")

if __name__ == "__main__":
    main()
