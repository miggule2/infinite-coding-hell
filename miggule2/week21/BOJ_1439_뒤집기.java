package week21;

import java.util.Scanner;

public class BOJ_1439_뒤집기 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        char prev = str.charAt(0);
        char first = prev;
        int count = 0;

        for(int i = 1; i < str.length(); i++) {
            if(str.charAt(i) != prev) {
                if(str.charAt(i) == first) count++;
            }
            prev = str.charAt(i);
        }

        if(prev != first) count++;
        System.out.println(count);
    }
}
