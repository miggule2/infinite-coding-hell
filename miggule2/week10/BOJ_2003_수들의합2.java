package week10;

import java.io.*;
import java.util.*;

public class BOJ_2003_수들의합2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0;
        int right = 0;
        int sum = arr[0];
        int result = 0;
        while(left < n-1 && right < n-1){
            if(sum == k){
                result++;
                sum -= arr[left++];
                sum += arr[++right];
            } else if(sum > k){
                if(left == right){
                    left++;
                    right++;
                    sum = arr[left];
                } else sum -= arr[left++];
            } else {
                sum += arr[++right];
            }
        }
        while(left <= right){
            if(sum == k){
                result++;
                break;
            } else if(sum > k){
                sum -= arr[left++];
            } else break;
        }
        System.out.println(result);
    }
}
