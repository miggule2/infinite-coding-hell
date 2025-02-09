package week7;

import java.util.*;
import java.io.*;

public class BOJ_2776_암기왕 {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());

        for(int i = 1; i <= n; i++){
            int a = Integer.parseInt(br.readLine());
            int[] arrayA = new int[a];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < a; j++){
                arrayA[j] = Integer.parseInt(st.nextToken());
            }

            int b = Integer.parseInt(br.readLine());
            int[] arrayB = new int[b];
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < b; j++){
                arrayB[j] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(arrayA);

            for(int num : arrayB){
                int left = 0;
                int right = arrayA.length - 1;
                boolean flag = false;
                while(left <= right){
                    int mid = left + (right - left) / 2;
                    if(num == arrayA[mid]) { flag = true; break;}
                    else if(num < arrayA[mid]) { right = mid - 1; }
                    else { left = mid + 1;}
                }
                if(flag) bw.write("1" + "\n");
                else bw.write("0" + "\n");
            }
        }
        bw.flush();
        bw.close();
    }
}
