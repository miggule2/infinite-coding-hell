package week7;

import java.util.*;
import java.io.*;

public class BOJ_2512_예산 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] array = new int[n];
        for(int i = 0; i < n; i++){
            array[i] = Integer.parseInt(st.nextToken());
        }

        long budget = Long.parseLong(br.readLine());

        long sum = 0;
        int max = Integer.MIN_VALUE;
        for(int i = 0; i < n; i++){
            sum += array[i];
            max = Math.max(max, array[i]);
        }

        if(sum <= budget){
            System.out.println(max);
        }
        else{
            int mid = 0;
            int answer = 0;
            int left = 0;
            int right = max;
            while(left <= right){
                sum = 0;
                mid = left + (right - left) / 2;
                for(int i = 0; i < n; i++){
                    if(array[i] <= mid) sum+=array[i];
                    else sum += mid;
                }
                if(sum <= budget){answer = mid;left = mid+1;}
                else {right = mid-1;}
            }
            System.out.println(answer);
        }
    }
}
