package week19;

import java.util.*;
import java.io.*;

public class BOJ_2644_촌수계산{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        HashMap<Integer,ArrayList<Integer>> map = new HashMap<>();
        HashSet<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();

        int n  = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int start =  Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        int total = Integer.parseInt(br.readLine());
        for(int i = 0; i < total; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if(!map.containsKey(a)){
                map.put(a,new ArrayList<>());
            }
            if(!map.containsKey(b)){
                map.put(b,new ArrayList<>());
            }

            map.get(a).add(b);
            map.get(b).add(a);
        }

        queue.add(start);
        visited.add(start);
        int result = 0;
        boolean flag = false;
        while(!queue.isEmpty()){

            int size = queue.size();
            for(int i =0 ; i < size; i++){
                int now =  queue.poll();
                if(now == end){flag = true; break;}
                for(int child : map.get(now)){
                    if(!visited.contains(child)){
                        queue.add(child);
                        visited.add(child);
                    }
                }
            }
            if(flag){break;}
            result++;
        }

        if(flag) System.out.println(result);
        else System.out.println(-1);

    }
}
