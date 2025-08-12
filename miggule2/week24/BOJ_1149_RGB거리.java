package week24;

import java.util.*;
import java.io.*;

public class BOJ_1149_RGB거리 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][3];

        for(int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            arr[i] = new int[]{a,b,c};
        }

        int[][] dp = new int[n][3];
        dp[0][0] = arr[0][0];
        dp[0][1] = arr[0][1];
        dp[0][2] = arr[0][2];

        System.out.println(Math.min(Math.min(recursion(arr,dp,n-1,0),recursion(arr,dp,n-1,1)),recursion(arr,dp,n-1,2)));
    }

    public static int recursion(int[][] arr, int[][] dp, int index, int rgb){
        if(dp[index][rgb] != 0) return dp[index][rgb];
        
        if(rgb == 0){
            dp[index][rgb] = arr[index][rgb] + Integer.min(recursion(arr, dp,index-1,1), recursion(arr,dp,index-1,2));
        } else {
            dp[index][rgb] = arr[index][rgb] + Integer.min(recursion(arr, dp,index-1,0), recursion(arr,dp,index-1,3-rgb));
        }

        return dp[index][rgb];
    }
    
}
