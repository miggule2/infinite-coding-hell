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

    public static int recursion(int[] dp, int num){
        if(num < 0 || num > 1000) return 0;

        if(dp[num] != 0) return dp[num];
        
        if(num%2 == 0){
            dp[num] = (recursion(dp,num/2)*recursion(dp,num/2) + recursion(dp,num/2-1)*recursion(dp,num/2-1)*2)%10007;
        } else {
            dp[num] = (recursion(dp,num/2)*recursion(dp,num/2+1) + recursion(dp,num/2-1)*recursion(dp,num/2)*2)%10007;
        }

        return dp[num];
    }
}
