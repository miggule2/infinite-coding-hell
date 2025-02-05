package week8;

import java.util.*;
import java.io.*;

public class BOJ_2343_기타레슨 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int cut = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            sum += arr[i];
        }

        int left = 0;
        int right = sum;
        while(left <= right){
            int count = 0;
            int partSum = 0;
            int mid = left + (right -left)/2;
            for(int i = 0; i < n; i++){
                if(arr[i] > mid) {count = Integer.MAX_VALUE-1; break;} // count = Integer.MAX_VALUE

                partSum += arr[i];

                if(partSum > mid){
                    count++;
                    partSum = 0;
                    i--;
                }
            }
            if(partSum != 0) count++;  // count가 최대 정수일 때, 오버플로우 에러 발생했음.
            if(count <= cut) right = mid-1;
            else left = mid + 1;
        }

        System.out.println(left);;
    }
}
