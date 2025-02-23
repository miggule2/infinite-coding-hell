def solve():
    import sys

    input = sys.stdin.readline

    # 1. 입력 받기
    N = int(input().strip())          # 수의 개수
    numbers = [input().strip() for _ in range(N)]  # 36진수 문자열들
    K = int(input().strip())          # 치환할 문자 개수

    # 2. 36진수를 10진수로 변환하는 함수 & 10진수를 36진수로 변환하는 함수
    def char_to_val(c):
        """'0'~'9' -> 0~9, 'A'~'Z' -> 10~35"""
        if c.isdigit():
            return ord(c) - ord('0')
        else:
            return ord(c) - ord('A') + 10

    def val_to_char(v):
        """0~9 -> '0'~'9', 10~35 -> 'A'~'Z'"""
        if v < 10:
            return chr(ord('0') + v)
        else:
            return chr(ord('A') + (v - 10))

    def base36_to_dec(s):
        """36진수 문자열 s를 10진수 정수로 변환"""
        val = 0
        for ch in s:
            val = val * 36 + char_to_val(ch)
        return val

    def dec_to_base36(num):
        """10진수 정수 num을 36진수 문자열로 변환"""
        if num == 0:
            return "0"
        digits = []
        while num > 0:
            digits.append(val_to_char(num % 36))
            num //=36
        return ''.join(reversed(digits))

    # 3. 원본 합 계산 (모든 수를 10진수로 변환 후 합)
    original_sum = 0
    for num in numbers:
        original_sum += base36_to_dec(num)

    # 4. 각 문자('0'~'9', 'A'~'Z')에 대한 이득 계산
    #    gain[c] = 해당 문자를 전부 'Z'(35)로 바꿨을 때 증가하는 총합
    gain = {c: 0 for c in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

    for num in numbers:
        length = len(num)
        for i, ch in enumerate(reversed(num)):
            # 자릿수: 36^i
            digit_val = char_to_val(ch)
            # (치환 후 35 - 원래값) * 36^i
            gain[ch] += (35 - digit_val) * (36 ** i)

    # 5. gain이 큰 문자 순으로 정렬 후 상위 K개의 이득 합 구하기
    #    (K=0인 경우도 고려하여, K>0일 때만 추가 이득 계산)
    gain_list = sorted(gain.values(), reverse=True)
    add_gain = sum(gain_list[:K]) if K > 0 else 0

    # 6. 최종 합 = original_sum + add_gain
    final_sum = original_sum + add_gain

    # 7. 최종 합을 36진수로 변환하여 출력
    print(dec_to_base36(final_sum))

solve()