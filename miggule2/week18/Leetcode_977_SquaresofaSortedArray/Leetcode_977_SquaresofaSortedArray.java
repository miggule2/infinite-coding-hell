package week18.Leetcode_977_SquaresofaSortedArray;

import java.util.Arrays;

public class Leetcode_977_SquaresofaSortedArray {
    public int[] sortedSquares(int[] nums) {
        for(int i = 0; i < nums.length; i++){
            nums[i] = (int)Math.pow(nums[i],2);
        }

        Arrays.sort(nums);
        return nums;
    }
}
