package week22;

import java.util.*;
import java.io.*;

public class BOJ_1874_스택수열 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        ArrayList<Character> result = new ArrayList<>();
        HashSet<Integer> visited = new HashSet<>();
        int max = 0;
        boolean flag = false;
        int prev = 0;
        for(int i = 0; i < n; i++){
            int num = Integer.parseInt(br.readLine());
            if(prev < num){
                for(int k = max+1; k <= num; k++){
                    result.add('+');
                }
                max = num;
            } else{
                for(int k = prev-1; k > num; k--){
                    if(!visited.contains(k)) {
                        flag=true;
                        break;
                    }
                }
            }
            result.add('-');
            visited.add(num);
            prev = num;

            if(flag) break;
        }

        if(flag) System.out.println("NO");
        else{
            for(Character c : result){
                System.out.println(c);
            }
        }
    }
}
