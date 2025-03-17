package week14.Leetcode_2206_DivideArrayIntoEqualPairs;

import java.util.Arrays;

public class Leetcode_2206_DivideArrayIntoEqualPairs_Sorting {
    class Solution {
        public boolean divideArray(int[] nums) {
            Arrays.sort(nums);

            boolean result = true;
            for(int i = 0; i < nums.length; i += 2){
                if(nums[i] != nums[i+1]){
                    result = false;
                    break;
                }
            }

            return result;
        }
    }
}
