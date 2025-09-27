package week24;

import java.util.*;
import java.io.*;

public class BOJ_1912_연속합 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int max = arr[0];
        int sum = arr[0];
        for(int i = 1; i < n; i++){
            if(sum < 0 && sum < arr[i]) {
                sum = arr[i];
                max = Math.max(max,sum);
                continue;
            }
            if(sum + arr[i] < 0){
                max = Math.max(max,sum);
                sum = arr[i];
            } else {
                sum += arr[i];
                max = Math.max(max,sum);
            }
        }

        System.out.println(max);
    }
}
