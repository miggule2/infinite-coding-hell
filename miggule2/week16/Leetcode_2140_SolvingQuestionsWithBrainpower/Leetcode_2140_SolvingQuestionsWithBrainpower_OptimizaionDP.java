package week16.Leetcode_2140_SolvingQuestionsWithBrainpower;

public class Leetcode_2140_SolvingQuestionsWithBrainpower_OptimizaionDP {
    class Solution {
        long[] dp;
        public long mostPoints(int[][] questions) {
            int len = questions.length;
            dp = new long[len];
            long result = recursion(questions,0);
            return result;
        }

        private long recursion(int[][] questions,int index){
            if(index >= questions.length) return 0;
            else if(dp[index] != 0) return dp[index];

            return dp[index] = Math.max(questions[index][0] + recursion(questions,index+questions[index][1]+1), recursion(questions,index+1));
        }
    }
}
