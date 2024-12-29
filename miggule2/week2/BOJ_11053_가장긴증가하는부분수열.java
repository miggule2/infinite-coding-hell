package week2;

import java.util.*;
import java.io.*;

public class BOJ_11053_가장긴증가하는부분수열{
    static int[] dp;
    static int[] array;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] s = br.readLine().split(" ");
        array = new int[n+1];
        dp = new int[n+1]; // 자기 전까지 이어진 숫자열의 길이를 저장하는 배열

        for(int i = 0; i < n; i++){
            array[i+1] = Integer.parseInt(s[i]);
        }

        // BottomUp 풀이
        // 1. for문 순회시 초기값 dp[자기자신] = 1을 대입한다.( 가능한 제일 짧은 숫자열 = 자기 자신만 배열로 갖는 숫자열 )
        // 2. (자기자신)-1 ~ 1까지 내려가며 자기보다 작은 요소를 만날 경우. dp[자기자신], dp[나보다 작은 요소]+1 중 큰 것을 dp[자기자신]에 대입
        // (연결된 숫자열이기에 dp[나보다 작은 요소]에 자기자신을 추가하면 그것 또한 연결된 숫자열을 만족함)
        // 3. 1,2번을 1~n 까지 반복하면, 각 순서(i)에 대해서 i-1 ~ 1까지 더 작은 요소 중 제일 긴 연결 요소와 연결해주는 것과 같음.

        for(int i = 1; i <= n; i++){
            dp[i] = 1;
            for(int j = i-1; j >= 1; j--){
                if(array[j] < array[i]){
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        int result = 0;
        for(int i = 1; i <= n; i++){
            result = Math.max(result, dp[i]);
        }
        System.out.println(result);
    }

}
