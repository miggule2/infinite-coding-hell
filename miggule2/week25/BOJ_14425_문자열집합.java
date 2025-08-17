package week25;

import java.util.*;
import java.io.*;

public class BOJ_14425_문자열집합 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] num = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = num[0];
        int m = num[1];

        HashSet<String> set = new HashSet<>();
        for(int i = 0; i < n; i++){
            set.add(br.readLine());
        }

        int count = 0;
        for(int i = 0; i < m; i++){
            if(set.contains(br.readLine())) count++;
        }

        System.out.println(count);
    }
}
