package week5;

import java.util.*;
import java.io.*;

public class BOJ_11404_플로이드 {
    static HashMap<Integer, LinkedList<int[]>> map = new HashMap<>();
    static int[][] result;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int v = Integer.parseInt(br.readLine());
        int e = Integer.parseInt(br.readLine());

        result = new int[v+1][v+1];
        for(int i = 1; i <= v; i++){
            map.put(i, new LinkedList<>());
        }

        for(int i = 0; i < e; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            map.get(start).add(new int[]{weight, end});
        }

        for(int i = 1; i <= v; i++){
            function(i);
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for(int i = 1; i <= v; i++){
            for(int j = 1; j <= v; j++){
                bw.write(Integer.toString(result[i][j]) + " ");
            }
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }

    private static void function(int station){
        int[] array = new int[result.length];
        Queue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));

        for(int i = 1; i < array.length; i++){
            array[i] = Integer.MAX_VALUE;
        }
        array[station] = 0;
        heap.add(new int[]{0, station});

        while(!heap.isEmpty()){
            int[] now = heap.poll();
            int nowWeight = now[0];
            int nowStop = now[1];
            for(int[] value : map.get(nowStop)){
                int valueWeight = value[0];
                int valueStop = value[1];
                if(array[valueStop] < valueWeight + nowWeight) continue;

                array[valueStop] = valueWeight + nowWeight;
                heap.add(new int[] {array[valueStop], valueStop});
            }
        }

        for(int i = 1; i < array.length; i++){
            if(array[i] == Integer.MAX_VALUE) array[i] = 0;
        }
        result[station] = array;
    }
}
