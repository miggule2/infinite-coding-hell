package week9;

import java.util.*;
import java.io.*;

public class BOJ_3273_두수의합 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] array = new int[n];
        for(int i = 0; i < n; i++){
            array[i] = Integer.parseInt(st.nextToken());
        }

        int x = Integer.parseInt(br.readLine());

        Arrays.sort(array);
        int result = 0;
        int left = 0;
        int right = array.length - 1;
        while(left < right){
            int sum = array[left] + array[right];
            if(sum == x){
                result++;
                left++;
            }
            else if(sum < x){
                left++;
            }
            else {
                right--;
            }
        }
        System.out.println(result);
    }
}
