package week6;

import java.util.*;
import java.io.*;

public class BOJ_1916_최소비용구하기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int v = Integer.parseInt(br.readLine());
        int e = Integer.parseInt(br.readLine());

        HashMap<Integer,ArrayList<int[]>> map = new HashMap<>();
        int[] array = new int[v+1];

        for(int i = 1; i <= v; i++){
            map.put(i, new ArrayList<>());
            array[i] = Integer.MAX_VALUE;
        }

        for(int i = 0; i < e; i++){
            st = new StringTokenizer(br.readLine());
            int start  = Integer.parseInt(st.nextToken());
            int end =  Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            map.get(start).add(new int[]{weight, end});
        }

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        Queue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a->a[0]));
        boolean[] visited = new boolean[v+1];
        array[start] = 0;
        heap.add(new int[]{0,start});
        while(!heap.isEmpty()){
            int[] now = heap.poll();
            int nowWeight = now[0];
            int nowStop = now[1];
            if(visited[nowStop]) continue;

            visited[nowStop] = true;
            for(int[] value : map.get(nowStop)){
                int valueWeight = value[0];
                int valueStop = value[1];
                if(visited[valueStop] || array[valueStop] <= array[nowStop] + valueWeight) continue;

                array[valueStop] = array[nowStop] + valueWeight;
                heap.add(new int[] {array[valueStop], valueStop});
            }
        }

        System.out.println(array[end]);
    }
}
