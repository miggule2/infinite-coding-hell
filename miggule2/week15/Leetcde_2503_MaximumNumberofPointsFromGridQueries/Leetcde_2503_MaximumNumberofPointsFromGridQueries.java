package week15.Leetcde_2503_MaximumNumberofPointsFromGridQueries;

import java.util.*;

public class Leetcde_2503_MaximumNumberofPointsFromGridQueries {
    class Solution {
        public int[] maxPoints(int[][] grid, int[] queries) {
            int row = grid.length;
            int col = grid[0].length;
            int gridSize = row * col;

            int[] result = new int[queries.length];
            int[] sortedQueries = new int[queries.length];
            Integer[] queryIndices = new Integer[queries.length];
            for (int i = 0; i < queries.length; i++) {
                sortedQueries[i] = queries[i];
                queryIndices[i] = i;
            }
            Arrays.sort(queryIndices, Comparator.comparingInt(i -> sortedQueries[i]));

            int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
            boolean[][] visited = new boolean[row][col];
            PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[2]));
            pq.offer(new int[]{0, 0, grid[0][0]});
            visited[0][0] = true;

            int count = 0;
            int queryIndex = 0;
            while (queryIndex < queries.length) {
                int query = sortedQueries[queryIndices[queryIndex]];
                while (!pq.isEmpty() && pq.peek()[2] < query) {
                    int[] cur = pq.poll();
                    count++;
                    for (int[] dir : dirs) {
                        int nextRow = cur[0] + dir[0];
                        int nextCol = cur[1] + dir[1];
                        if (nextRow >= 0 && nextRow < row && nextCol >= 0 && nextCol < col && !visited[nextRow][nextCol]) {
                            pq.offer(new int[]{nextRow, nextCol, grid[nextRow][nextCol]});
                            visited[nextRow][nextCol] = true;
                        }
                    }
                }
                result[queryIndices[queryIndex]] = count;
                queryIndex++;
            }

            return result;
        }
    }
}
