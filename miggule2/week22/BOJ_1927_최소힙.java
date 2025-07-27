package week22;

import java.util.*;
import java.io.*;

public class BOJ_1927_최소힙 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n ; i++){
            int k = Integer.parseInt(br.readLine());
            if(k==0){
                if(minHeap.isEmpty()) System.out.println(0);
                else System.out.println(minHeap.poll());
            } else {
                minHeap.add(k);
            }
        }
    }
}
