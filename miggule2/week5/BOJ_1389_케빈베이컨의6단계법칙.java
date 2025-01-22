package week5;

import java.util.*;
import java.io.*;

public class BOJ_1389_케빈베이컨의6단계법칙 {
    static boolean[][] map;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        map = new boolean[n+1][n+1];

        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            map[a][b] = true;
            map[b][a] = true;
        }

        int min = Integer.MAX_VALUE;
        int result = 1;

        for(int i = 1; i <= n; i++){
            int sum = bfs(i);
            if(sum < min){ result = i; min = sum;}
        }

        System.out.println(result);
    }

    private static int bfs(int self){
        Queue<Integer> queue = new LinkedList<>();
        Integer[] array = new Integer[map.length];
        array[self] = 0;
        queue.add(self);
        int count = 1;

        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i = 0; i < size; i++){
                int key = queue.poll();
                for(int j = 0; j < map.length; j++){
                    if(!map[key][j]) continue;
                    if(array[j] != null) continue;

                    array[j] = count;
                    queue.add(j);
                }
            }
            count++;
        }

        int sum = 0;
        for(int i = 1; i < array.length; i++){
            sum += array[i];
        }

        return sum;
    }
}
