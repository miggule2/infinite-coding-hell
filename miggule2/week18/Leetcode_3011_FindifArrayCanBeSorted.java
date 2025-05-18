package week18;

import java.util.Arrays;

public class Leetcode_3011_FindifArrayCanBeSorted {
    public boolean canSortArray(int[] nums) {
        int[] setBitsArray = bitsArray(nums);
        System.out.println(Arrays.toString(setBitsArray));
        int previousMax = 0;
        int max = nums[0];
        for(int i = 1; i < setBitsArray.length; i++){
            if(setBitsArray[i-1] == setBitsArray[i]) max = Math.max(max,nums[i]);
            else{
                previousMax = max;
                max = nums[i];
            }
            if(previousMax > nums[i]) return false;
        }
        return true;
    }

    private int[] bitsArray(int[] nums){
        int[] returnArray = new int[nums.length];

        int i = 0;
        for(int num : nums){
            int count = 0;
            while(num != 0){
                if(num == 1) {count++; break;}
                else if(num >= 2 && num < 4) num -= 2;
                else if(num >= 4 && num < 8) num -= 4;
                else if(num >= 8 && num < 16) num -= 8;
                else if(num >= 16 && num < 32) num -= 16;
                else if(num >= 32 && num < 64) num -= 32;
                else if(num >= 64 && num < 128) num -= 64;
                else if(num >= 128 && num < 256) num -= 128;
                else num -= 256;

                count++;
            }
            returnArray[i] = count;
            i++;
        }
        return returnArray;
    }
}
