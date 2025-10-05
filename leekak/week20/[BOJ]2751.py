import sys

def solve():
    try:
        N = int(sys.stdin.readline().strip())
    except:
        return
      
    arr = []
    for _ in range(N):
        arr.append(int(sys.stdin.readline().strip()))

    arr.sort() 

    sys.stdout.write('\n'.join(map(str, arr)))

if __name__ == "__main__":
    solve()
