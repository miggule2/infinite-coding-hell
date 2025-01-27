package week5;

import java.util.*;
import java.io.*;

public class BOJ_1753_최단경로 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int v = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        // 기준이 되는 시작점 입력
        st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());

        HashMap<Integer, ArrayList<int[]>> map = new HashMap<>(); // 그래프 탐색을 위한 그래프
        // 다익스트라 알고리즘을 위한 배열 초기화 & 모든 노드에 대응하는 빈 연결리스트 추가
        int[] result = new int[v+1];
        for(int i = 1; i <= v; i++){
            map.put(i, new ArrayList<>());
            result[i] = Integer.MAX_VALUE;
        }

        // 그래프 초기화
        for(int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            map.get(start).add(new int[]{weight, end});
        }

        // 다익스트라 알고리즘 시작.
        // 다익스트라 알고리즘은 특정 노드를 기준으로 모든 노드까지의 최소 비용을 구하는 알고리즘.
        Queue<int[]> queue = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        result[k] = 0; // 자기 자신까지의 거리는 0
        queue.add(new int[] {0,k}); // 제일 처음 시작은 기준 노드

        while(!queue.isEmpty()){
            int[] now = queue.poll(); // 사이클마다 비용이 가장 작은 비용이 드는 ( 비용, 노드 ) 쌍을 꺼냄. (이러면 다익스트라 초기 버전의 모든 노드를 방문하는 경우에서 불필요한 동작들을 하지 않아도 됨.)
            for(int[] value : map.get(now[1])){  // 해당 노드와 붙어있는 노드 꺼내기 ( 다음 노드라고 지칭 )
                if(result[value[1]] <= value[0]+now[0]) continue; // 다음 노드까지의 비용 <= 현재 노드의 비용 + 현재 노드에서 다음 노드까지 비용 이면 갱신 필요 없음.

                // 위의 조건이 아닌 경우(다음 노드까지의 비용이 갱신되었을 경우)
                result[value[1]] = value[0]+now[0]; // 배열에서 값을 갱신해주고
                queue.add(new int[] {result[value[1]], value[1]}); // 힙애 ( 비용, 다음 노드 )를 넣어준다
            }
        }

        for(int i = 1; i <= v; i++){
            if(result[i] == Integer.MAX_VALUE){
                System.out.println("INF");
            }
            else System.out.println(result[i]);
        }
    }
}
