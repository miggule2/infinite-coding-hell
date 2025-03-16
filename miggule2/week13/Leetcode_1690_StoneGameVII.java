package week13;

public class Leetcode_1690_StoneGameVII {
    class Solution {
        public int stoneGameVII(int[] stones) {
            int[][] dp = new int[stones.length][stones.length];
            for(int i = stones.length - 2; i >= 0; i--){
                int total = stones[i];
                for(int j = i+1; j < stones.length; j++){
                    total += stones[j];
                    dp[i][j] = Math.max(total - stones[i] - dp[i+1][j], total - stones[j] - dp[i][j-1]);
                }
            }
            return dp[0][stones.length-1];
        }
    }
}
