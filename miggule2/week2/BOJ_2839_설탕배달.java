package week2;

import java.util.Scanner;

public class BOJ_2839_설탕배달 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); sc.nextLine();
        int[] array = new int[5001];
        array[0] = -1;
        array[1] = -1;
        array[2] = -1;
        array[3] = 1;
        array[4] = -1;
        array[5] = 1;

        for(int i = 6; i <= n; i++) {
            int a = array[i - 3] != -1 ? array[i - 3] + 1 : 1000000;
            int b = array[i - 5] != -1 ? array[i - 5] + 1 : 1000000;

            if (a == b && a == 1000000) {
                array[i] = -1;
            } else {
                array[i] = Math.min(a, b);
            }
        }

        System.out.println(array[n]);
    }
}
