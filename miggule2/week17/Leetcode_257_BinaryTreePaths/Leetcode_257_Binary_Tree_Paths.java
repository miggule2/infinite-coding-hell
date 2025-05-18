package week17.Leetcode_257_BinaryTreePaths;

import java.util.*;

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

public class Leetcode_257_Binary_Tree_Paths {
    public List<String> binaryTreePaths(TreeNode root) {
        ArrayList<String> result = new ArrayList<>();
        tree(root,"",result);
        return result;
    }

    private void tree(TreeNode node, String path, ArrayList<String> result){
        if(node==null) return;
        if(node.right == null &&  node.left == null) {
            result.add(path+node.val);
            return;
        }

        tree(node.left, path+node.val+"->",result);
        tree(node.right, path+node.val+"->",result);

        return;
    }
}
