package week23;

import java.io.*;

public class BOJ_10799_쇠막대기_CharInput {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        char[] arr = new char[str.length()];

        for(int i = 0; i < arr.length; i++){
            arr[i] = str.charAt(i);
        }

        int stack = 0;
        int result = 0;
        char prev = '(';
        for(char c : arr){
            if(c == '(') stack++;
            else {
                stack--;
                if(prev == '('){
                    result += stack;
                } else {
                    result ++;
                }
            }
            prev = c;
        }
        System.out.println(result);
    }
}
