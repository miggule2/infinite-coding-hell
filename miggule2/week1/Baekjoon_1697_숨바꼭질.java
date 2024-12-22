package week1;

import java.util.*;

public class Baekjoon_1697_숨바꼭질 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int start = sc.nextInt();
        int end = sc.nextInt(); sc.nextLine();

        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[100000+1];
        queue.add(start);
        int level = 0;
        boolean flag = false;

        while(!queue.isEmpty()){
            int queueSize = queue.size();
            for(int i = 0; i < queueSize; i++){
                int node = queue.poll();
                visited[node] = true;
                if(node == end) {flag = true; break;}

                if(node-1 >= 0 && node-1 <= 100000 && !visited[node-1]) queue.add(node-1);
                if(node+1 >= 0 && node+1 <= 100000 && !visited[node+1]) queue.add(node+1);
                if(node*2 >= 0 && node*2 <= 100000 && !visited[node*2]) queue.add(node*2);
            }
            if(flag) break;
            level++;
        }

        System.out.println(level);
    }
}
