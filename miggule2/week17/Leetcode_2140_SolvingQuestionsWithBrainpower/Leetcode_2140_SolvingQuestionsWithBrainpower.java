package week17.Leetcode_2140_SolvingQuestionsWithBrainpower;

public class Leetcode_2140_SolvingQuestionsWithBrainpower {
    class Solution {
        long[] dp;
        public long mostPoints(int[][] questions) {
            int len = questions.length;
            dp = new long[len];
            return recursion(questions,0);
        }

        private long recursion(int[][] questions,int index){
            if(index == questions.length-1) return dp[index] = questions[index][0];
            if(index+questions[index][1]+1 >= questions.length) return dp[index] = Math.max(questions[index][0], recursion(questions,index+1));

            long jump = 0;
            if(dp[index+questions[index][1]+1] != 0) jump = dp[index+questions[index][1]+1];
            else {
                jump = recursion(questions,index+questions[index][1]+1);
                dp[index+questions[index][1]+1] = jump;
            }

            long next = 0;
            if(dp[index+1] != 0) next = dp[index+1];
            else {
                next = recursion(questions,index+1);
                dp[index+1] = next;
            }

            return dp[index] = Math.max(questions[index][0] + jump, next);
        }
    }
}
