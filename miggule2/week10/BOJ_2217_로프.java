package week10;

import java.io.*;
import java.util.Arrays;

public class BOJ_2217_로프 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(arr);
        int max = Integer.MIN_VALUE;
        for(int i = 0; i < arr.length; i++){
            max = Math.max(max, (i+1)*arr[arr.length-i-1]);
        }
        System.out.println(max);
    }
}
