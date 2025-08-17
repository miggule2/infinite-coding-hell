package week25;

import java.util.*;
import java.io.*;

public class BOJ_1932_정수삼각형 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        // 원래는 이차원 배열로 할 예정이었으나 각 배열에 들어가는 배열의 크기가 달라져 HashMap에 배열을 넣는 방식으로 결정 
        HashMap<Integer,int[]> map = new HashMap<>();
        HashMap<Integer,int[]> dp = new HashMap<>();

        // 입력
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
        // 초기화
        dp.get(0)[0] = map.get(0)[0];

        // 마지막 배열에 나올 수 있는 최적값 대입
        for(int i = 0; i < n; i++){
            recursion(dp,map,n-1,i);
        }

        //출력
        int result = Integer.MIN_VALUE;
        for(int i = 0; i < n; i++){
            result = Math.max(result,dp.get(n-1)[i]);
        }

        System.out.println(result);
    }

    // dp 로직 구현
    // 1. 삼각형의 제일 끝에서 나올 수 있는 모든 요소의 최댓값을 구한 뒤 그 최댓값을 출력
    // 2. dp배열의 값은 자기자신 + 부모 둘 중 dp값이 더 큰 요소를 대입
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
