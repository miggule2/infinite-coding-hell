package week17.Leetcode_2415_ReverseOddLevelsofBinaryTree;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Leetcode_2415_ReverseOddLevelsofBinaryTree {
    public TreeNode reverseOddLevels(TreeNode root) {
        if(root.left == null && root.right == null) return root;
        LinkedList<TreeNode> listLeft = new LinkedList<>();
        LinkedList<TreeNode> listRight = new LinkedList<>();
        int level = 1;

        int temp = root.right.val;
        root.right.val = root.left.val;
        root.left.val = temp;
        listLeft.add(root.left);
        listRight.add(root.right);
        level++;

        while(!listLeft.isEmpty() && !listRight.isEmpty()){
            System.out.println(level);
            for(int i = 0; i < Math.pow(2,level-2); i++){
                TreeNode node1 = listLeft.removeFirst();
                TreeNode node2 = listRight.removeFirst();

                if(node1.left == null) continue;

                if(level%2 == 1){
                    temp = node2.right.val;
                    node2.right.val = node1.left.val;
                    node1.left.val = temp;

                    temp = node2.left.val;
                    node2.left.val = node1.right.val;
                    node1.right.val = temp;
                }
                listLeft.add(node1.left);
                listLeft.add(node1.right);
                listRight.add(node2.right);
                listRight.add(node2.left);
            }
            level++;
        }
        return root;
    }
}
