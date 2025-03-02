package week11;

import java.io.*;
import java.util.*;

public class BOJ_1946_신입사원 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for(int i = 0; i < t; i++){
            int n = Integer.parseInt(br.readLine());
            int cnt = 0;

            int[][] arr = new int[n][2];
            for(int j = 0; j < n; j++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                arr[j][0] = Integer.parseInt(st.nextToken());
                arr[j][1] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(arr, Comparator.comparingInt(a -> a[0]));

            int min = Integer.MAX_VALUE;
            for(int j = 0; j < n; j++){
                if(min > arr[j][1]){
                    min = arr[j][1];
                    cnt++;
                }
            }

            System.out.println(cnt);
        }
    }
}
