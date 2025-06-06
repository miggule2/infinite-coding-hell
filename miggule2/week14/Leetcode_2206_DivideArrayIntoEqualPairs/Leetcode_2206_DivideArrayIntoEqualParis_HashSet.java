package week14.Leetcode_2206_DivideArrayIntoEqualPairs;

import java.util.HashSet;

public class Leetcode_2206_DivideArrayIntoEqualParis_HashSet {
    class Solution {
        public boolean divideArray(int[] nums) {
            HashSet<Integer> set = new HashSet<>();

            for(int num : nums){
                if(set.contains(num)) set.remove(num);
                else set.add(num);
            }

            return set.isEmpty();
        }
    }
}
