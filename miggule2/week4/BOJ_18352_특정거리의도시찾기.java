package week4;

import java.util.*;
import java.io.*;

public class BOJ_18352_특정거리의도시찾기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int nodes = Integer.parseInt(st.nextToken());
        int edges = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(st.nextToken());
        Queue<Integer> queue = new LinkedList<>();
        HashMap<Integer, Integer> map = new HashMap<>();
        HashMap<Integer, ArrayList<Integer>> edge = new HashMap<>();

        for(int i = 0; i < edges; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if(!edge.containsKey(a)){edge.put(a, new ArrayList<>());}
            edge.get(a).add(b);
        }

        for(int num : edge.get(start)){
            queue.add(num);
        }
        map.put(start,0);

        int count = 1;
        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i = 0; i < size; i++){
                int key = queue.poll();

                if(map.containsKey(key)) continue;

                map.put(key, count);
                if(edge.containsKey(key)){
                    for (int num : edge.get(key)) {
                        queue.add(num);
                    }
                }
            }
            count++;
        }

        ArrayList<Integer> ans = new ArrayList<>();
        for(int num : map.keySet()){
            if(map.get(num)==k) {
                ans.add(num);
            }
        }

        if(ans.isEmpty()) System.out.println(-1);
        else {
            Collections.sort(ans);
            for(int num : ans){
                System.out.println(num);
            }
        }
    }
}
