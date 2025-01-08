package week4;

import java.util.*;
import java.io.*;

public class BOJ_2468_안전영역 {
    static int[][] array;
    static boolean[][] visited;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int max = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        array = new int[n][n];

        for(int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++){
                array[i][j] = Integer.parseInt(st.nextToken());
                max = Math.max(max, array[i][j]);
            }
        }

        for(int h = 0; h <= max; h++){
            int result = 0;
            visited = new boolean[n][n];
            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    if(array[i][j] > h && !visited[i][j]){
                        dfs(i,j,h);
                        result++;
                    }
                }
            }
            heap.add(-result);
        }

        System.out.println(-(heap.poll()));
    }

    private static void dfs(int x, int y, int h){
        if(array[x][y] <= h) return;
        visited[x][y] = true;

        if(x-1 >= 0 && array[x-1][y] > h && !visited[x-1][y]) dfs(x-1, y, h);
        if(x+1 < array.length && array[x+1][y] > h && !visited[x+1][y]) dfs(x+1, y, h);
        if(y-1 >= 0 && array[x][y-1] > h && !visited[x][y-1]) dfs(x, y-1, h);
        if(y+1 < array.length && array[x][y+1] > h && !visited[x][y+1]) dfs(x, y+1, h);
    }
}
