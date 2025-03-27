package week15.Leetcode_3169_CountDaysWithoutMeetings;

import java.util.*;

public class Leetcode_3169_CountDaysWithoutMeetings_SimpleLogic {
    class Solution {
        public int countDays(int days, int[][] meetings) {
            TreeMap<Integer,Integer> map = new TreeMap<>();
            for(int[] meeting : meetings){
                map.put(meeting[0],map.getOrDefault(meeting[0],0)+1);
                map.put(meeting[1],map.getOrDefault(meeting[1],0)-1);
            }
            int pre = 0;
            int onMeeting = 0;
            int result = 0;
            for(int key : map.keySet()){
                if(onMeeting == 0) {
                    result += key-pre-1;
                }

                onMeeting += map.get(key);

                pre = key;
            }

            result += days-pre;

            return result;
        }
    }
}
