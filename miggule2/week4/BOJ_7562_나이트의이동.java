// 나이트의 최소 이동 거리를 구하는 문제이기에 bfs 사용.
// bfs 같은 경우 위,아래,좌,우를 확인하는 문제가 일반적이지만, 이런식으로 활용되어 나와도 이제는 풀이를 조금만 변형하여 해결할 수 있었음.
// 코드가 지저분하게 늘어지는 걸 방지하기 위해, 다음 칸을 조사하는 코드는 배열과 반복문을 통해 조금 더 빠르고 깔끔하게 풀이작성할 수 있도록 해야겠음.

// 반복문의 경우 초기화 할 필요가 있는 경우, 개별적으로 항상 체크하기!(초기화가 필요한 요소요소 전부)
// 반복문 끝에 초기화 몰아 코드를 적는 것도 좋아보임.
package week4;

import java.util.*;
import java.io.*;

public class BOJ_7562_나이트의이동 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Queue<int[]> queue = new LinkedList<>();
        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++){
            int size = Integer.parseInt(br.readLine());
            String[] stringStart = br.readLine().split(" ");
            int[] start = {Integer.parseInt(stringStart[0]), Integer.parseInt(stringStart[1])};
            String[] stringEnd = br.readLine().split(" ");
            int[] end = {Integer.parseInt(stringEnd[0]), Integer.parseInt(stringEnd[1])};

            boolean[][] visited = new boolean[size][size]; // 방문 노드
            int count = 0;
            boolean flag = false;
            queue.add(start);
            visited[start[0]][start[1]] = true;

            // bfs풀이
            // 1. 첫번째 노드를 queue에 넣어둔 채로 시작.
            // 2. 큐에 들어있는 요소 개수만큼 한 사이클 반복
            // 3. 한 사이클에는 큐에 들어 있는 모든 노드에 대해 다음 갈 수 있는 모든 칸에 대해서 0보다 큰지, 노드 전체 크기보다 작은지 확인하여, 나이트가 갈 수 있는 다음 칸을 큐에 대입, 방문 노드에 추가.
            // 4. 한 사이클 마다 시행 횟수++ 하면서 목적지에 닿은 노드가 있는 순간 반복문 중단.
            while(!queue.isEmpty()){
                int queueSize = queue.size();
                for(int j = 0; j < queueSize; j++){
                    int[] node = queue.poll();
                    int x = node[0];
                    int y = node[1];

                    if(x == end[0] && y == end[1]){flag = true; break;}

                    if(x+2 < size && y+1 < size && !visited[x+2][y+1]){queue.add(new int[]{x+2, y+1}); visited[x+2][y+1] = true;}
                    if(x+1 < size && y+2 <size && !visited[x+1][y+2]){queue.add(new int[]{x+1, y+2}); visited[x+1][y+2] = true;}
                    if(x+2 < size && y-1 >= 0 && !visited[x+2][y-1]){queue.add(new int[]{x+2, y-1}); visited[x+2][y-1] = true;}
                    if(x+1 < size && y-2 >= 0 && !visited[x+1][y-2]){queue.add(new int[]{x+1, y-2}); visited[x+1][y-2] = true;}
                    if(x-2 >= 0 && y+1 <size && !visited[x-2][y+1]){queue.add(new int[]{x-2, y+1}); visited[x-2][y+1] = true;}
                    if(x-1 >= 0 && y+2 <size && !visited[x-1][y+2]){queue.add(new int[]{x-1, y+2}); visited[x-1][y+2] = true;}
                    if(x-2 >= 0 && y-1 >= 0 && !visited[x-2][y-1]){queue.add(new int[]{x-2, y-1}); visited[x-2][y-1] = true;}
                    if(x-1 >= 0 && y-2 >= 0 && !visited[x-1][y-2]){queue.add(new int[]{x-1, y-2}); visited[x-1][y-2] = true;}
                }
                if(flag) break;
                count++;
            }
            System.out.println(count);
            queue.clear();
        }
    }
}
