package week1;

import java.util.Queue;
import java.util.LinkedList;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Baekjoon_2178_미로탐색 {
    static int endX;
    static int endY;
    static int[][] array;
    static boolean[][] visited;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] num = br.readLine().split(" ");
        endX = Integer.parseInt(num[0]);
        endY = Integer.parseInt(num[1]);
        array = new int[endX][endY];
        visited = new boolean[endX][endY];
        for(int i = 0; i < endX; i++){
            String[] numList = br.readLine().split("");
            for(int j = 0; j < endY; j++){
                array[i][j] = Integer.parseInt(numList[j]);
                if(array[i][j] == 0 ) visited[i][j] = true;
            }
        }

        System.out.println(bfs(0,0));
    }

    static int bfs(int row, int col){
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {row,col});
        visited[row][col] = true;
        int now = 1;

        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i = 0; i < size; i++){
                int[] node = queue.poll();
                int x = node[0];
                int y = node[1];
                if(x == endX-1 && y == endY-1) {return now;}

                if(x-1 >= 0 && x-1 < array.length && !visited[x-1][y]) {queue.add(new int[] {x-1,y}); visited[x-1][y] = true;}
                if(x+1 >= 0 && x+1 < array.length && !visited[x+1][y]) {queue.add(new int[] {x+1,y}); visited[x+1][y] = true;}
                if(y-1 >= 0 && y-1 < array[0].length && !visited[x][y-1]) {queue.add(new int[] {x,y-1}); visited[x][y-1] = true;}
                if(y+1 >= 0 && y+1 < array[0].length && !visited[x][y+1]) {queue.add(new int[] {x,y+1}); visited[x][y+1] = true;}
            }
            now++;
        }
        return now;
    }
}
