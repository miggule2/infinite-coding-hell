package week6;

import java.util.*;
import java.io.*;

public class BOJ_1916_최소비용구하기_다익스트라시간초과 {
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
        array[start] = 0;
        heap.add(new int[]{0,start});
        while(!heap.isEmpty()){
            int[] now = heap.poll();
            int nowWeight = now[0];
            int nowStop = now[1];
            for(int[] value : map.get(nowStop)){
                int valueWeight = value[0];
                int valueStop = value[1];
                if(array[valueStop] <= nowWeight + valueWeight) continue;

                array[valueStop] = nowWeight + valueWeight;
                heap.add(new int[] {array[valueStop], valueStop});
            }
        }

        System.out.println(array[end]);
    }
}
