HM = 100000000
MASK64 = (1 << 64) - 1

def PNUhash(x: int, salt: int) -> int:
    x = (x + salt) & MASK64
    x = ((x ^ (x >> 30)) * 0xbf58476d1ce4e5b9) & MASK64
    x = ((x ^ (x >> 27)) * 0x94d049bb133111eb) & MASK64
    x = (x ^ (x >> 31)) & MASK64
    return x % HM

if __name__ == "__main__":
    for i in range(1000678980115, 1000678980216):
        print(f"PNUhash({i}) = {PNUhash(i, 32):8d}")

    K = 345_679_232_990
    print("K =", K, "=>", PNUhash(K, 32))
    