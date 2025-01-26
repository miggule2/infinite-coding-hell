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
        Integer[] times = new Integer[100000 + 1]; // visited가 의미 있는 경우엔 Integer == null 인 경우를 빼주면 되지만, 이번 경우엔 int[]에 Integer.MAX_VALUE를 대입해서 푸는 게 더 효율적이여 보임.
        queue.add(start);
        times[start] = 0; // 시작 칸의 경우 0으로 초기화

        //bfs풀이 시작
        // 1. 제일 처음엔 start만 queue에 담긴채로 시작.
        // 2. +1,-1 했을 경우와 *2 했을 경우의 시간(비용)이 다르기 때문에 이미 방문한 노드더라도, 나중에 방문한 경우가 시간이 덜 걸릴 수 있기 때문에
        // times[다음] 과 times[현재]+1 or +0 을 비교해서 더 작은 경우에 갱신해주고, queue에 다음 숫자를 삽입
        // 3. 2번 과정을 반복
        while (!queue.isEmpty()) {
            int now = queue.poll();

            if (now+1 <= 100000 && (times[now+1] == null || times[now+1] > times[now]+1)) {queue.add(now+1); times[now+1] = times[now]+1;}
            if (now-1 >= 0 && (times[now-1] == null || times[now-1] > times[now]+1)) {queue.add(now-1); times[now-1] = times[now]+1;}
            if (2*now <= 100000 && (times[2*now] == null || times[2*now] > times[now])) {queue.add(2*now); times[2*now] = times[now];}
        }

        System.out.println(times[end]);
    }
}