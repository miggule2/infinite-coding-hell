package week21.BOJ_1931_회의실배정;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class BOJ_1931_회의실배정 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n =  Integer.parseInt(br.readLine());

        StringTokenizer st;
        LinkedList<int[]> list = new LinkedList<>();
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            list.add(new int[]{a,b});
        }

        list.sort((a,b)->{
            if(a[1]==b[1]){return Integer.compare(a[0],b[0]);}
            else return Integer.compare(a[1],b[1]);
        });

        int endtime = 0;
        int count = 0;
        for (int[] ints : list) {
            if(ints[0] >= endtime){
                endtime = ints[1];
                count++;
            }
        }

        System.out.println(count);
    }
}
