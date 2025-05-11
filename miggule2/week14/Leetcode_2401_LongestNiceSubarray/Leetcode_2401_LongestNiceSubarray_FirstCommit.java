package week14.Leetcode_2401_LongestNiceSubarray;

public class Leetcode_2401_LongestNiceSubarray_FirstCommit {
    class Solution {
        public int longestNiceSubarray(int[] nums) {
            int start = 0;
            int end = 1;
            int max = 1;

            int xor = nums[0];
            while(end < nums.length){
                if((xor & nums[end]) != 0) {

                    max = Math.max(max,end-start);
                    start = end-1;
                    xor = nums[end];
                    while(start > 0){
                        if((xor & nums[start]) != 0){
                            break;
                        }
                        xor ^= nums[start];
                        start--;
                    }
                    start++;
                }
                else {
                    xor ^= nums[end];
                }
                end++;
            }
            max = Math.max(max,end-start);
            return max;
        }
    }
}
