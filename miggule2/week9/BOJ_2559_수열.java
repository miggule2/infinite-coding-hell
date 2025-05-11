package week9;

import java.io.*;
import java.util.*;

public class BOJ_2559_수열 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] array = new int[n];
        for(int i = 0; i < n; i++){
            array[i] = Integer.parseInt(st.nextToken());
        }

        int sum = 0;
        for(int i = 0; i < k; i++){
            sum += array[i];
        }
        int result = sum;
        for(int i = k; i < array.length; i++){
            sum += array[i];
            sum -= array[i-k];
            result = Math.max(result,sum);
        }
        System.out.println(result);
    }
}
