package week14.Leetcode_2206_DivideArrayIntoEqualPairs;

public class Leetcode_2206_DivideArrayIntoEqualPairs_BooleanArray {
    class Solution {
        public boolean divideArray(int[] nums) {
            int max = Integer.MIN_VALUE;
            for(int num : nums){
                max = Math.max(max,num);
            }

            boolean[] boolArr = new boolean[max+1];

            for(int num : nums){
                boolArr[num] = !boolArr[num];
            }

            for(boolean bool : boolArr){
                if(bool) return false;
            }

            return true;
        }
    }
}
