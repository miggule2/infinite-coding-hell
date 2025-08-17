package week25;

import java.util.*;
import java.io.*;

public class BOJ_1932_정수삼각형 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashMap<Integer,int[]> map = new HashMap<>();
        HashMap<Integer,int[]> dp = new HashMap<>();

        for(int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            map.put(i,new int[i+1]);
            Arrays.fill(map.get(i),-1);
            dp.put(i,new int[i+1]);
            Arrays.fill(dp.get(i),-1);
            for(int j = 0; j < i+1; j++){
                map.get(i)[j] = Integer.parseInt(st.nextToken());
            }
        }
        dp.get(0)[0] = map.get(0)[0];

        for(int i = 0; i < n; i++){
            recursion(dp,map,n-1,i);
        }

        int result = Integer.MIN_VALUE;
        for(int i = 0; i < n; i++){
            result = Math.max(result,dp.get(n-1)[i]);
        }

        System.out.println(result);
    }

    public static int recursion(HashMap<Integer,int[]> dp, HashMap<Integer,int[]> map,int level, int index){
        if(dp.get(level)[index] != -1) return dp.get(level)[index]; 
        
        if(index == 0) {
            dp.get(level)[index] = map.get(level)[index] + recursion(dp,map,level-1,0);
        } else if(index == level) {
            dp.get(level)[index] = map.get(level)[index] + recursion(dp,map,level-1,level-1);
        } else {
            dp.get(level)[index] = map.get(level)[index] + Math.max(recursion(dp,map,level-1,index-1), recursion(dp,map,level-1,index));
        }
        return dp.get(level)[index];
    }
}
