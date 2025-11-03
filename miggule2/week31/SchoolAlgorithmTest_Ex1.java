package week31;

import java.util.*;
import java.io.*;

public class SchoolAlgorithmTest_Ex1 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            int red = Integer.parseInt(st.nextToken());
            int blue = Integer.parseInt(st.nextToken());
            int total = red+blue;
            int[][] arr = new int[red+blue][2];

            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < red; j++){
                int num = Integer.parseInt(st.nextToken());
                arr[j] = new int[]{num,0};
            }

            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < blue; j++){
                int num = Integer.parseInt(st.nextToken());
                arr[red+j] = new int[]{num,1};
            }

            Arrays.sort(arr,(o1,o2) -> {
                if(o1[0] != o2[0]) return o1[0] - o2[0];
                return o1[1] - o2[1];
            });
            int redSortingResult = total%2 == 0 ? arr[total/2-1][1] : arr[(total+1)/2-1][1];

            Arrays.sort(arr,(o1,o2) -> {
                if(o1[0] != o2[0]) return o1[0] - o2[0];
                return o2[1] - o1[1];
            });
            int blueSortingResult = total%2 == 0 ? arr[total/2-1][1] : arr[(total+1)/2-1][1];

            String result;
            if(redSortingResult == blueSortingResult) result = redSortingResult == 0 ? "R" : "B";
            else result = "RB";

            System.out.println(result);
        }

    }
}
