package week18;

public class Leetcode_75_SortColors {
    public void sortColors(int[] nums) {
        for(int i = 1; i < nums.length; i++){
            for(int j = i-1; j >= 0; j--){
                if(nums[j+1]>=nums[j]) break;
                else{
                    int temp = nums[j+1];
                    nums[j+1] = nums[j];
                    nums[j] = temp;
                }
            }
        }
    }
}
