package week3;

import java.io.*;

public class BOJ_2579_계단오르기 {

    static int[] array;
    static int[] resultArray;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        array = new int[n+1];
        resultArray = new int[n+1];
        for(int i = 1; i <= n; i++){
            array[i] = Integer.parseInt(br.readLine());
        }

        System.out.println(recursion(n));
    }

    private static int recursion(int index){
        if(index <= 0) return 0;
        if(resultArray[index]!=0) return resultArray[index];

        return resultArray[index] = array[index] + Math.max(recursion(index - 2), recursion(index - 3)+array[index-1]);
    }
}
