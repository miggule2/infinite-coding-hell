package week19;

import java.util.*;
import java.io.*;

public class BOJ_1158_Yosephus {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        String[] numString = str.split(" ");
        int a = Integer.parseInt(numString[0]);
        int b = Integer.parseInt(numString[1]);
        boolean[] boolArr = new boolean[a];

        int[] result = new int[a];
        int index = 0;
        for(int i =0; i < a; i++){
            int count = 0;
            while(count<b){
                if(index >= a){
                    index = 0;
                    continue;
                }
                if(boolArr[index]){
                    index++;
                    continue;
                }
                index++;
                count++;
            }
            boolArr[index-1] = true;
            result[i]=index;
        }

        System.out.print("<");
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i != result.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println(">");
    }
}
