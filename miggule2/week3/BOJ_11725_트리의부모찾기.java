package week3;

import java.util.*;
import java.io.*;

public class BOJ_11725_트리의부모찾기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>(); // 간선 정보 저장
        HashSet<Integer> visited = new HashSet<>(); // dfs할 때, 방문했던 노드 저장
        Stack<Integer> stack = new Stack<>(); // dfs시 사용할 스택
        int[] result = new int[n+1];

        for(int i = 0; i < n-1;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if(!map.containsKey(a)){ map.put(a,new ArrayList<>());}
            map.get(a).add(b);
            if(!map.containsKey(b)){ map.put(b,new ArrayList<>());}
            map.get(b).add(a);
        }

        // 1은 항상 최상단에 있기 때문에, 1부터 시작.
        stack.add(1);
        visited.add(1);

        // dfs 풀이
        // 1. 제일 먼저 1(루트 노드)에 연결되어 있는 노드들의 부모를 1로 설정.
        // 2. 1과 연결된 노드들을 stack에 push.
        // 3. 다음 사이클에서 stack에 있는 노드(key)를 팝해서 그와 연결된 노드 중 방문한 적 없는 노드(부모가 정해지지 않은 노드)의 부모를 key로 설정. 그리고 그 노드들을 다시 stack에 푸시.
        // 4. stack에 들어갈 노드가 없을 때까지(모든 노드를 방문할 때까지) 3을 반복.
        // 5. 모든 노드의 방문이 끝나면 모든 노드의 부모가 찾아진 것이기에 실행을 중단.
        while(!stack.isEmpty()){
            int size = stack.size();
            for(int i = 0; i < size; i++){
                int key = stack.pop();
                for(int value : map.get(key)){
                    if(visited.contains(value)) continue;
                    result[value] = key;
                    visited.add(value);
                    stack.push(value);
                }
            }
        }

        for(int i = 2; i <= n; i++){
            bw.write(Integer.toString(result[i]) + "\n");
        }
        bw.flush();
        bw.close();
    }
}
