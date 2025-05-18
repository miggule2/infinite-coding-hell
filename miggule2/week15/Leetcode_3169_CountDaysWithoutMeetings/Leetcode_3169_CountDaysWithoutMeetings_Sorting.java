package week15.Leetcode_3169_CountDaysWithoutMeetings;

import java.util.*;

public class Leetcode_3169_CountDaysWithoutMeetings_Sorting {
    class Solution {
        public int countDays(int days, int[][] meetings) {
            Arrays.sort(meetings,Comparator.comparingInt((int[] o) -> o[0]));

            int maxEnd = 0;
            int result = 0;

            for(int[] meeting : meetings){
                int start = meeting[0];
                int end = meeting[1];

                if(start > maxEnd+1){
                    result += start-maxEnd-1;
                }

                maxEnd = Math.max(maxEnd,end);
            }
            result += days - maxEnd;

            return result;
        }
    }
}
