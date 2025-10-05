package week31;

import java.util.*;
import java.io.*;

public class SchoolAlgorithmTest_Ex2 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++){
            int size = Integer.parseInt(br.readLine());
            long[] arr = new long[size];
            long[] max_dp = new long[size];

            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < size; j++){
                arr[j] = Long.parseLong(st.nextToken());
            }

            if(size == 1) {System.out.println(0); continue;}

            max_dp[size-1] = 0L;
            max_dp[size-2] = arr[size-1];
            for(int j = size-3; j >= 0; j--){
                max_dp[j] = Math.max(max_dp[j+1],0L) + arr[j+1];
            }

            for(int j = 0; j < size; j++){
                max_dp[j] = Math.max(max_dp[j],0L);
            }

            for(long num : max_dp){
                System.out.print(num+" ");
            }
            System.out.println();
        }
    }
}
