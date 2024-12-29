package week2;

import java.util.*;
import java.io.*;

public class BOJ_2606_바이러스 {
    static HashMap<Integer,ArrayList<Integer>> map = new HashMap<>();
    static HashSet<Integer> visited = new HashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int numNode = Integer.parseInt(br.readLine());
        int numEdges = Integer.parseInt(br.readLine());

        for(int i = 0; i < numEdges; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if(!map.containsKey(a)) { map.put(a, new ArrayList<>()); }
            if(!map.containsKey(b)) { map.put(b, new ArrayList<>()); }
            map.get(a).add(b);
            map.get(b).add(a);
        }

        // 1과 연결된 간선이 없는 채로 dfs 실행할 경우 nullPointerException 발생 가능성 있기에, 예외처리
        if(!map.containsKey(1)) {
            System.out.println(0);
            return;
        }

        dfs(1);
        System.out.println(visited.size()-1);
    }

    private static void dfs(int node){
        for(int value : map.get(node)){
            if(visited.contains(value)) continue;
            visited.add(value);
            dfs(value);
        }
    }
}
