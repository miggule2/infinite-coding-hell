package week10;

import java.util.Scanner;

public class BOJ_5585_거스름돈 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        n = 1000-n;
        int result = 0;

        while(n > 0){
            if(n - 500 >= 0){
                n -= 500;
            } else if(n - 100 >= 0){
                n -= 100;
            } else if(n - 50 >= 0){
                n -= 50;
            } else if(n - 10 >= 0){
                n -= 10;
            } else if(n - 5 >= 0){
                n -= 5;
            } else {
                n -= 1;
            }
            result ++;
        }
        System.out.println(result);
    }
}
