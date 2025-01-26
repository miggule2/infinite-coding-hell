import math

a, b = map(int, input().split())
c, d = map(int, input().split())

denomi = b*d
numera = a*d + b*c
gcd = math.gcd(denomi, numera)
print(int(numera/gcd), int(denomi/gcd))