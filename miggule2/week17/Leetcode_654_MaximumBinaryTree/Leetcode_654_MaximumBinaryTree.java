package week17.Leetcode_654_MaximumBinaryTree;

import java.util.Arrays;

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
      this.val = val;
      this.left = left;
      this.right = right;
    }
}

public class Leetcode_654_MaximumBinaryTree {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        if(nums.length == 0) return null;
        int max = -1;
        int max_index = 0;

        for(int i = 0; i < nums.length; i++){
            if(nums[i] > max) {
                max = nums[i];
                max_index = i;
            }
        }

        TreeNode root = new TreeNode(max);
        root.left = constructMaximumBinaryTree(Arrays.copyOfRange(nums,0,max_index));
        root.right = constructMaximumBinaryTree(Arrays.copyOfRange(nums,max_index+1,nums.length));

        return root;
    }
}
