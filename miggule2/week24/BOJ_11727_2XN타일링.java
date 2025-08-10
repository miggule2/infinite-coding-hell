package week24;

import java.util.*;

public class BOJ_11727_2XN타일링 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] dp = new int[1001];
        dp[1] = 1;
        dp[2] = 3;
        dp[3] = 5;
        recursion(dp,n);
        System.out.println(dp[n]);
    }

    // dp 문제
    // 1. 1,2,3 단계의 경우엔 기본값으로 잡음
    // 2. 짝수의 경우 각 단계의 직사각형을 반으로 나눠 나온 숫자의 dp값 곱 + 중간을 2*1,2*2 로 잊고 나머지 도형간의 곱을 더한 값을 dp값을 저장
    // 3. 홀수의 경우 각 단계의 직사각형을 반으로 (n/2,n/2+1)로 나눠 나온 숫자의 dp값 곱 + 중간을 2*1,2*2 로 잊고 나머지 도형간의 곱을 더한 값을 dp값을 저장
    // 4. recursion(n)의 값을 출력(dp[n])
    public static int recursion(int[] dp, int num){
        if(num < 0 || num > 1000) return 0;

        // 이미 있는 값은 그대로 리턴
        if(dp[num] != 0) return dp[num]; 
        
        if(num%2 == 0){
            //짝수의 경우
            dp[num] = (recursion(dp,num/2)*recursion(dp,num/2) + recursion(dp,num/2-1)*recursion(dp,num/2-1)*2)%10007;
        } else {
            //홀수의 경우
            dp[num] = (recursion(dp,num/2)*recursion(dp,num/2+1) + recursion(dp,num/2-1)*recursion(dp,num/2)*2)%10007;
        }

        return dp[num];
    }
}
