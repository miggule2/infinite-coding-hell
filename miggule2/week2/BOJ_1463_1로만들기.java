package week2;

import java.util.Scanner;

public class BOJ_1463_1로만들기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); sc.nextLine();
        int[] array = new int[n+1];
        array[1] = 0;

        for(int i = 2; i <= n; i++){
            int a = array[i-1]+1;
            int b = 1000000;
            int c = 1000000;
            if(i%2 == 0) b = array[i/2]+1;
            if(i%3 == 0) c = array[i/3]+1;

            array[i] = Math.min(a,Math.min(b,c));
        }

        System.out.println(array[n]);
    }
}
