class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 지그재그가 필요 없는 경우
        if numRows == 1 or numRows >= len(s):
            return s

        # 각 줄을 담을 리스트
        rows = [""] * numRows

        current_row = 0 # 현재 줄 번호
        going_down = False  # 현재 이동 방향

        for ch in s:
            rows[current_row] += ch

            # 맨 위 혹은 맨 아래에서 방향 전환
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # 위 또는 아래로 이동
            current_row += 1 if going_down else -1

        # 모든 줄을 합쳐 최종 문자열 생성
        return "".join(rows)
