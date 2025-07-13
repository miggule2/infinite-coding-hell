package week20;

import java.io.*;
import java.util.*;

public class BOJ_11047_동전0_Greedy {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = Integer.parseInt(br.readLine());
        }

        int count = 0;
        while(k>0){
            for(int i=n-1;i>=0;i--){
                if(arr[i]<=k) {
                    k -= arr[i];
                    count++;
                    break;
                }
            }
        }

        System.out.println(count);
    }
}
