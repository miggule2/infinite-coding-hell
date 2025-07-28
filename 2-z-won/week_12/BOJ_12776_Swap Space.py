import sys
input = sys.stdin.readline

def main():
    n = int(input())
    pos = []   # b[i] - a[i] >= 0
    neg = []   # b[i] - a[i] <  0

    for _ in range(n):
        a, b = map(int, input().split())
        if b >= a:
            pos.append((a, b))
        else:
            neg.append((a, b))

    pos.sort(key=lambda x: x[0])
    neg.sort(key=lambda x: -x[1])

    s = 0      
    req = 0    

    for a, b in pos:
        req = max(req, a - s)
        s += (b - a)

    for a, b in neg:
        req = max(req, a - s)
        s += (b - a)

    print(max(req, 0))


if __name__ == "__main__":
    main()
