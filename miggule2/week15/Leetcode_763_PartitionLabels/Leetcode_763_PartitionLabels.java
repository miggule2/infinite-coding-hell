package week15.Leetcode_763_PartitionLabels;

import java.util.*;

public class Leetcode_763_PartitionLabels {
    class Solution {
        public List<Integer> partitionLabels(String s) {
            ArrayList<int[]> list = new ArrayList<>();
            HashSet<Character> discovered = new HashSet<>();

            for(int i = 0; i < s.length(); i++){
                char c = s.charAt(i);
                if(discovered.contains(c)) continue;
                else {
                    for(int j = s.length()-1; j >= 0 ;j--){
                        if(s.charAt(j) == c){
                            list.add(new int[]{i,j});
                            discovered.add(c);
                            break;
                        }
                    }
                }
            }

            Collections.sort(list,Comparator.comparingInt((int[] o) -> o[0]));
            int[][] tempArr = new int[discovered.size()][2];
            int now = 0;
            for(int[] arr : list){
                if(arr[0] > tempArr[now][1]){
                    now++;
                    tempArr[now][0] = arr[0];
                    tempArr[now][1] = arr[1];
                } else{
                    tempArr[now][1] = Math.max(tempArr[now][1],arr[1]);
                }
            }

            List<Integer> result = new ArrayList<>();
            for(int i = 0; i < tempArr.length; i++){
                if(i != 0 && tempArr[i][0] == 0 && tempArr[i][1]==0) break;
                result.add(tempArr[i][1]- tempArr[i][0] + 1);
            }

            return result;
        }
    }
}
