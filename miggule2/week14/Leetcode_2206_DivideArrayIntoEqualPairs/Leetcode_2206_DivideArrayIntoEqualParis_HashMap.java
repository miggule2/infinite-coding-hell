package week14.Leetcode_2206_DivideArrayIntoEqualPairs;

import java.util.HashMap;

public class Leetcode_2206_DivideArrayIntoEqualParis_HashMap {
    class Solution {
        public boolean divideArray(int[] nums) {
            HashMap<Integer,Integer> countMap = new HashMap<>();

            for(int num : nums){
                countMap.put(num,countMap.getOrDefault(num,0)+1);
            }

            for(int num : countMap.keySet()){
                if(countMap.get(num) % 2 == 1) return false;
            }
            return true;
        }
    }
}
