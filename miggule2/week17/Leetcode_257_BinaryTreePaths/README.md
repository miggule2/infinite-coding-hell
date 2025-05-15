## 해결법
### 1. dfs(재귀 이용)
* 재귀를 이용해서 dfs로 루트에서 리프까지 모든 경로를 찾음.

#### dfs 중단 조건
* 자기 자신이 null 인 경우 -> __return__
* __자식들이 아무것도 없는 경우 -> 리프이기 때문에__ 리프에서 자기 자신까지 경로를 결과에 대입 후 return

#### dfs의 진행
* 파라미터로 자식과 이때까지의 경로를 담은 문자열을 보내줌

#### 코드
```java
class Solution {
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
```
