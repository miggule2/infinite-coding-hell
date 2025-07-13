package week20;

import java.util.Scanner;

public class BOJ_16953_AtoB_Greedy {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        int count = 1;
        // 그리디 알고리즘
        // 문제 조건은 a->b 조건이지만
        // b->a 로 설계하여 해결
        while(b > a){
            // 숫자 마지막 숫자(1)을 떼는 것이 /2 하는 것보다 무조건 작기 때문에(최소 카운트를 찾는 문제) 이 조건을 먼저 처리
            if(b%10==1) {
                b = b/10;
                count++;
                continue;
            }

            // 이 부분에서 문제 발생
            // 이 조건이 없으면 홀수를 /2할 때 버림이 발생하여 반복문 정상 진행
            // 하지만 홀수를 /2하는 경우는 존재할 수 없으므로 진행 종료돼야함.
            if(b%2==1) break;
            else b=b/2;

            count++;
        }

        if(b==a) System.out.println(count);
        else System.out.println(-1);
    }
}
