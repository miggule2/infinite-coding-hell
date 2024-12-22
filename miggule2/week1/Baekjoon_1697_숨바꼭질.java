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
        visited[start] = true;
        int level = 0;
        boolean flag = false;

        // bfs 풀이 시작
        // 1. queue에서 나오는 각 숫자에 -1,+1,*2를 한 숫자를 queue에 대입 + 방문 표시.(방문한 적이 있는 곳은 패스)
        // 2. for문 처음을 기준으로 queue에 담긴 숫자개수에 1의 과정을 반복한 것을 하나의 레벨로 지정.
        // 3. 1,2의 과정을 반복하다 queue에서 꺼낸 숫자가 end와 같을 경우 break하고 당시 그 레벨이 답.
        while(!queue.isEmpty()){
            int queueSize = queue.size();
            for(int i = 0; i < queueSize; i++){  //(주의) for(int i = 0; i < queue.size(); i++) 이런 식으로 코드 작성할 경우 사이클마다 size()호출
                int node = queue.poll();
                if(node == end) {flag = true; break;} //queue에서 숫자를 꺼내어 end와 같을 경우

                if(node-1 >= 0 && node-1 <= 100000 && !visited[node-1]) {queue.add(node-1); visited[node-1] = true;} // ">= 0"는 오버플로우 방지
                if(node+1 >= 0 && node+1 <= 100000 && !visited[node+1]) {queue.add(node+1); visited[node+1] = true;} // " <= 10000 "은 문제에서 제시된 숫자 범위
                if(node*2 >= 0 && node*2 <= 100000 && !visited[node*2]) {queue.add(node*2); visited[node*2] = true;} // !visited[node]는 방문한 곳 패스
            }
            if(flag) break;
            level++;
        }

        System.out.println(level);
    }
}
