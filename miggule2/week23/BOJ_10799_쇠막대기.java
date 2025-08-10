package week23;

import java.io.*;

public class BOJ_10799_쇠막대기 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = br.readLine().split("");

        int stack = 0;
        int result = 0;
        String prev = "(";
        for(String str : arr){
            if(str.equals("(")) stack++;
            else {
                stack--;
                if(prev.equals("(")){
                    result += stack;
                } else {
                    result ++;
                }
            }
            prev = str;
        }
        System.out.println(result);
    }
}
