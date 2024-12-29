package week2;

import java.util.Scanner;

public class BOJ_2748_피보나치수2_BottomUp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); sc.nextLine();
        long[] visited = new long[n+1];
        visited[0] = 0;
        visited[1] = 1;
        for(int i = 2; i <= n; i++){
            visited[i] = visited[i-1] + visited[i-2];
        }

        System.out.println(visited[n]);
    }
}
