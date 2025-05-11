package week11;

import java.util.Scanner;

public class BOJ_1789_수들의합 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        int count = 0;
        long i = 1;
        while(true){
            if(i*2 >= n) {count++; break;}
            n -= i++;
            count++;
        }

        System.out.println(count);
    }
}
