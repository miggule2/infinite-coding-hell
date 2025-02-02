package week7;

import java.util.Scanner;

public class BOJ_1072_게임 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong(); // 오버플로우를 피하기 위해 long 타입 사용
        long b = sc.nextLong();
        sc.nextLine();

        long target = (b*100/a)+1; // 목표값(원래 퍼센트 + 1) 설정

        if(target >= 100) {        // 목표값이 100을 넘어가는 경우는 답을 찾을 수 없음
            System.out.println(-1);
            return;
        }

        // 중복값이 있을 경우 가장 왼쪽 값을 찾는 이분 탐색
        int left = 0;
        int right = Integer.MAX_VALUE;
        while(left < right){ // 중복값이 없을 때와 다르게 left <= index < right 로 범위 설정
            int mid = left + (right - left)/2; // 오버플로우를 피하기 위한 (left + right)/2 연산
            int result = (int)((((double)b+mid) / (a+mid))*100); // 백분율을 처리하기 위한 방법 ( 위에 있는 새로운 방법이 훨씬 간단함 )
            if(result >= target) right = mid; // right = mid로 설정한 이유는 다음 사이클 때, mid값을 포함하여 탐색하여 하나도 빠짐없이 가장 왼쪽 값을 탐색할 수 있음.
            else left = mid + 1;
        }

        System.out.println(left);
    }
}
