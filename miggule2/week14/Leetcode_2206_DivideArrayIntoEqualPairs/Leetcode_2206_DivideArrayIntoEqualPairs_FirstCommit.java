package week14.Leetcode_2206_DivideArrayIntoEqualPairs;

public class Leetcode_2206_DivideArrayIntoEqualPairs_FirstCommit {
    class Solution {
        public boolean divideArray(int[] nums) {
            int[] array = new int[500+1];

            for(int num : nums){
                array[num]++;
            }

            boolean result = true;

            for(int count : array){
                if(count % 2 == 1) {result = false; break;}
            }

            return result;
        }
    }
}
