package week5;

import java.util.*;
import java.io.*;

public class BOJ_1753_최단경로 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int v = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());

        HashMap<Integer, ArrayList<int[]>> map = new HashMap<>();
        int[] result = new int[v+1];
        for(int i = 1; i <= v; i++){
            map.put(i, new ArrayList<>());
            result[i] = Integer.MAX_VALUE;
        }

        for(int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            map.get(start).add(new int[]{weight, end});
        }

        Queue<int[]> queue = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        result[k] = 0;
        queue.add(new int[] {0,k});

        while(!queue.isEmpty()){
            int[] now = queue.poll();
            for(int[] value : map.get(now[1])){
                if(result[value[1]] <= value[0]+now[0]) continue;

                result[value[1]] = value[0]+now[0];
                queue.add(new int[] {result[value[1]], value[1]});
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
