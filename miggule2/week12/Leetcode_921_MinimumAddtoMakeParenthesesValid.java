package week12;

//스택 개념을 활용해서 쉽게 풀 수 있었던 문제

public class Leetcode_921_MinimumAddtoMakeParenthesesValid {
    public int minAddToMakeValid(String s) {
        int left = 0;
        int right = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '(') left++; // 왼쪽 괄호를 기준으로 스택 채우기
            else {
                if(left == 0) right++; // 스택이 비어있을 경우
                else left--; // 왼쪽 괄호 있으면 하나 POP
            }
        }

        return left + right;
    }
}
