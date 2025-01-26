package week6;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_13549_숨바꼭질3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int start = sc.nextInt();
        int end = sc.nextInt();
        sc.nextLine();

        Queue<Integer> queue = new LinkedList<>();
        Integer[] times = new Integer[100000 + 1];
        queue.add(start);
        times[start] = 0;

        while (!queue.isEmpty()) {
            int now = queue.poll();

            if (now+1 <= 100000 && (times[now+1] == null || times[now+1] > times[now]+1)) {queue.add(now+1); times[now+1] = times[now]+1;}
            if (now-1 >= 0 && (times[now-1] == null || times[now-1] > times[now]+1)) {queue.add(now-1); times[now-1] = times[now]+1;}
            if (2*now <= 100000 && (times[2*now] == null || times[2*now] > times[now])) {queue.add(2*now); times[2*now] = times[now];}
        }

        System.out.println(times[end]);
    }
}