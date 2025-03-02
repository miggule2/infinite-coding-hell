package week11;

import java.io.*;
import java.util.*;

public class BOJ_13305_주유소 {
    static int[] distances;
    static int[] prices;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        distances = new int[n-1];
        prices = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n-1; i++){
            distances[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i< n; i++){
            prices[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(greedy(0,n-1));
    }

    private static long greedy(int start, int end){
        if(start == end) return 0;
        int index = end;
        int min = Integer.MAX_VALUE;
        for(int i = start; i < end; i++){
            if(min >= prices[i]){
                min = prices[i];
                index = i;
            }
        }
        long distance = 0;
        for(int i = index; i < end; i++){
            distance += distances[i];
        }
        long price = prices[index]*distance;
        return greedy(start,index) + price;
    }
}
