// 반복문의 경우 초기화 할 필요가 있는 경우, 개별적으로 항상 체크하기!(초기화가 필요한 요소요소 전부)
// 반복문 끝에 초기화 몰아 코드를 적는 것도 좋아보임.
package week4;

import java.util.*;
import java.io.*;

public class BOJ_7562_나이트의이동 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Queue<int[]> queue = new LinkedList<>();
        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++){
            int size = Integer.parseInt(br.readLine());
            String[] stringStart = br.readLine().split(" ");
            int[] start = {Integer.parseInt(stringStart[0]), Integer.parseInt(stringStart[1])};
            String[] stringEnd = br.readLine().split(" ");
            int[] end = {Integer.parseInt(stringEnd[0]), Integer.parseInt(stringEnd[1])};

            boolean[][] visited = new boolean[size][size];
            int count = 0;
            boolean flag = false;
            queue.add(start);
            visited[start[0]][start[1]] = true;

            while(!queue.isEmpty()){
                int queueSize = queue.size();
                for(int j = 0; j < queueSize; j++){
                    int[] node = queue.poll();
                    int x = node[0];
                    int y = node[1];

                    if(x == end[0] && y == end[1]){flag = true; break;}

                    if(x+2 < size && y+1 < size && !visited[x+2][y+1]){queue.add(new int[]{x+2, y+1}); visited[x+2][y+1] = true;}
                    if(x+1 < size && y+2 <size && !visited[x+1][y+2]){queue.add(new int[]{x+1, y+2}); visited[x+1][y+2] = true;}
                    if(x+2 < size && y-1 >= 0 && !visited[x+2][y-1]){queue.add(new int[]{x+2, y-1}); visited[x+2][y-1] = true;}
                    if(x+1 < size && y-2 >= 0 && !visited[x+1][y-2]){queue.add(new int[]{x+1, y-2}); visited[x+1][y-2] = true;}
                    if(x-2 >= 0 && y+1 <size && !visited[x-2][y+1]){queue.add(new int[]{x-2, y+1}); visited[x-2][y+1] = true;}
                    if(x-1 >= 0 && y+2 <size && !visited[x-1][y+2]){queue.add(new int[]{x-1, y+2}); visited[x-1][y+2] = true;}
                    if(x-2 >= 0 && y-1 >= 0 && !visited[x-2][y-1]){queue.add(new int[]{x-2, y-1}); visited[x-2][y-1] = true;}
                    if(x-1 >= 0 && y-2 >= 0 && !visited[x-1][y-2]){queue.add(new int[]{x-1, y-2}); visited[x-1][y-2] = true;}
                }
                if(flag) break;
                count++;
            }
            System.out.println(count);
            queue.clear();
        }
    }
}
