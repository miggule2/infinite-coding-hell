package week3;

import java.util.ArrayList;
import java.io.*;
import java.util.Comparator;

public class BOJ_2667_단지번호붙이기 {
    static int[][] array;
    static int result;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        array = new int[n][n];
        int total = 0;
        ArrayList<Integer> list = new ArrayList<>();

        for(int i = 0; i < n; i++){
            String[] nums = br.readLine().split("");
            for(int j = 0; j < n; j++){
                array[i][j] = Integer.parseInt(nums[j]);
            }
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(array[i][j] == 1){
                    dfs(i,j);
                    total++;
                    list.add(result);
                    result = 0;
                }
            }
        }
        list.sort(Comparator.naturalOrder());
        System.out.println(total);
        for(int num : list){
            System.out.println(num);
        }
    }

    private static void dfs(int x, int y){
        if(array[x][y] == 0) return;
        array[x][y] = 0;
        result++;
        if(x-1 >= 0) dfs(x-1, y);
        if(x+1 < array.length) dfs(x+1, y);
        if(y-1 >= 0) dfs(x, y-1);
        if(y+1 < array[0].length) dfs(x, y+1);
    }
}
