package week8;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2343_기타레슨_수정코드 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int cut = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        int sum = 0;
        int max = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            sum += arr[i];
            max = Math.max(max, arr[i]);
        }

        int left = max;
        int right = sum;
        while(left <= right){
            int count = 0;
            int partSum = 0;
            int mid = left + (right -left)/2;
            for(int i = 0; i < n; i++){
                if(partSum + arr[i] > mid){
                    count++;
                    partSum = 0;
                }
                partSum += arr[i];
            }
            if(partSum != 0) count++;
            if(count <= cut) right = mid-1;
            else left = mid + 1;
        }

        System.out.println(left);
    }
}
