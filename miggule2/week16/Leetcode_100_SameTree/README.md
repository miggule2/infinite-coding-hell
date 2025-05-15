## 해결법
### 1. 재귀
```java
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
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null) return true;
        else if(p == null || q == null) return false;

        return (p.val==q.val)&&isSameTree(p.left,q.left)&&isSameTree(p.right,q.right);
    }
}
```
* 재귀로 p, q 각각의 서브 트리를 타고 내려가며 동일한 작업을 수행해주면 됐던 문제.
* 재귀는 __끝을 정의하는게 시작이자 끝.__
* 이 문제에서는 p,q 동시에 null이면 true를 반환 / p,q 중 하나만 null이면 같은 위치에 있는데, 하나만 null임을 뜻하기에 false 반환
* return 문에는 ```p,q 노드의 값을 비교 && 왼쪽 서브트리 재귀 && 오른쪽 서브트리 재귀``` 를 수행하여 전부 true일 경우에만 true 반환.

   
* __시간복잡도__ : 최악 ```O(max(p노드,q노드))```