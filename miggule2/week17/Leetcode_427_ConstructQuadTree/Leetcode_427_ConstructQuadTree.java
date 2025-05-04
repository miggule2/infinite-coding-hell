package week17.Leetcode_427_ConstructQuadTree;

/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;


    public Node() {
        this.val = false;
        this.isLeaf = false;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }

    public Node(boolean val, boolean isLeaf) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }

    public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
}
*/


public class Leetcode_427_ConstructQuadTree {
    public Node construct(int[][] grid) {
        return createTree(0,0,grid.length,grid);
    }

    // 이 문제의 핵심 메서드
    // 재귀적으로 접근하여 조건을 만족하는 경우 자식이 없고, 조건을 만족 안 하는 경우에는 4개의 자식에 대해서 같은 메서드를 적용하여 결과적으로 모든 트리의 노드를 생성
    private Node createTree(int row, int col, int distance, int[][] grid){
        Node result = new Node();

        // 해당 레벨에서의 모든 요소가 같은 경우
        if(check(row,col,distance,grid)) {
            boolean value = grid[row][col] == 1 ? true : false;
            return result = new Node(value, true);
        }
        // 모든 요소가 같지 않은 경우
        // 재귀적으로 접근하여 4개의 자식에 대하여 같은 메서드 적용
        else{
            result.val = true;
            result.isLeaf = false;
            result.topLeft = createTree(row,col,distance/2,grid);
            result.topRight = createTree(row,col+distance/2,distance/2,grid);
            result.bottomLeft = createTree(row+distance/2,col,distance/2,grid);
            result.bottomRight = createTree(row+distance/2,col+distance/2,distance/2,grid);
            return result;
        }
    }

    // 트리를 내려가면 내려갈 수록 체크해야할 grid의 한 변의 길이가 달리지기에 시작 행,열을 받고 길이도 받아 모든 요소가 같으면 true, 다르면 false 리턴
    private boolean check(int row, int col, int distance, int[][] grid){
        for(int i = row; i < row+distance;  i++){
            for(int j = col; j < col+distance; j++){
                if(grid[row][col] != grid[i][j]) return false;
            }
        }

        return true;
    }
}
