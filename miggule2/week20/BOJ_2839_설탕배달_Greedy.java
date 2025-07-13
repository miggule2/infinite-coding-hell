package week20;

import java.util.Scanner;

public class BOJ_2839_설탕배달_Greedy {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int count = 0;

        while(n>=0){
            if(n%5 == 0) {
                System.out.println(count+n/5);
                return;
            } else {
                n -= 3;
                count++;
            }
        }
        System.out.println(-1);
    }
}
