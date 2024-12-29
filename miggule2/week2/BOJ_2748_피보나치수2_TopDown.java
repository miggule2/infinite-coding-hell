package week2;

import java.util.Scanner;

public class BOJ_2748_피보나치수2_TopDown {
    static long[] visited;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); sc.nextLine();
        visited = new long[n+1];
        visited[0] = 0;
        visited[1] = 1;
        System.out.println(dp(n));
    }

    private static long dp(int n){
        if(n==0) return n;
        if(visited[n]!=0) return visited[n];

        return visited[n] = dp(n-1) + dp(n-2);
    }
}
