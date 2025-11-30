package week34;

import java.util.ArrayList;

public class 프로그래머스_석유시추 {
    static int count = 0;
    static int minY = Integer.MAX_VALUE;
    static int maxY = 0;

    public int solution(int[][] land) {
        int result = 0;

        boolean[][] visited = new boolean[land.length][land[0].length];
        ArrayList<Integer> amountList = new ArrayList<>();
        ArrayList<int[]> rangeList = new ArrayList<>();

        for(int i = 0; i < land[0].length; i++){
            for(int j = 0; j < land.length; j++){
                dfs(land,visited,j,i);

                if(count != 0){
                    amountList.add(count);
                    rangeList.add(new int[]{minY,maxY});

                    count = 0;
                    minY = 0;
                    maxY = 0;
                }
            }
        }

        int j = 0;
        for(int i = 0; i < land[0].length;i++){
            int temp = 0;
            for(int[] range : rangeList){
                if(i >= range[0] && i <= range[1]) temp += amountList.get(j);
                j++;
            }
            result = Math.max(result, temp);
        }

        for(int[] range : rangeList){
            System.out.println(range[0]);
        }
        return result;
    }

    private void dfs(int[][] land, boolean[][] visited, int x, int y){
        if(land[x][y] == 0 || visited[x][y]) return;

        count++;
        visited[x][y] = true;
        minY = Math.min(minY, y);
        maxY = Math.max(maxY, y);
        if(x-1 >= 0) dfs(land,visited,x-1,y);
        if(x+1 < visited.length) dfs(land,visited,x+1,y);
        if(y-1 >= 0) dfs(land,visited,x,y-1);
        if(y+1 < visited[0].length) dfs(land,visited,x,y+1);
    }
}
