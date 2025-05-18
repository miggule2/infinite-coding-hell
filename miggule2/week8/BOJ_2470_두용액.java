package week8;

import java.io.*;
import java.util.*;

public class BOJ_2470_두용액 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] array = new int[n];
        for(int i = 0; i < n; i++){
            array[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(array);

        int left = 0;
        int right = array.length - 1;
        int min = Integer.MAX_VALUE;
        int[] answer = new int[2];

        while(left < right){
            int sum = array[left] + array[right];
            if(min > Math.abs(sum)){
                min = Math.abs(sum);
                answer[0] = array[left];
                answer[1] = array[right];
            }

            if(sum == 0) break;
            else if(sum < 0) left++;
            else right--;
        }

        System.out.println(answer[0] + " " + answer[1]);
    }
}
