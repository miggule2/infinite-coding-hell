package week13;

import java.util.HashMap;
import java.util.ArrayList;
import java.util.Arrays;

public class Programmers_개인정보수집유효기간 {
    class Solution {
        public int[] solution(String today, String[] terms, String[] privacies) {
            HashMap<String, Integer> map = new HashMap<>();

            int[] todayDate = dateStringToInt(today);

            for(int i = 0; i < terms.length; i++){
                String[] term = terms[i].split(" ");
                map.put(term[0],Integer.parseInt(term[1]));
            }

            ArrayList<Integer> tempArray = new ArrayList<>();

            for(int i = 0; i < privacies.length; i++){
                String[] privacy = privacies[i].split(" ");
                int[] date = dateStringToInt(privacy[0]);
                String target = privacy[1];

                date[1] += map.get(target);
                date = correctDate(date);

                if(isDeleteData(date,todayDate)) {
                    tempArray.add(i+1);
                }
            }

            Integer[] arr = tempArray.toArray(new Integer[0]);
            int[] answer = new int[arr.length];
            for(int i = 0; i < answer.length; i++){
                answer[i] = arr[i];
            }
            return answer;
        }

        private int[] dateStringToInt(String dateString){
            int[] result = new int[3];
            String[] dateStringArray = dateString.split("\\.");
            for(int i = 0; i< 3; i++){
                result[i] = Integer.parseInt(dateStringArray[i]);
            }
            return result;
        }

        private int[] correctDate(int[] date){
            int times = date[1]/12;
            int mod = date[1]%12;

            if(mod == 0) {
                date[0] += times-1;
                date[1] = 12;
            } else {
                date[0] += times;
                date[1] = mod;
            }

            return date;
        }

        private boolean isDeleteData(int[] targetDate, int[] today){
            return !(targetDate[0]>today[0] || (targetDate[0]==today[0] && targetDate[1] > today[1]) || (targetDate[0]==today[0] && targetDate[1] == today[1] && targetDate[2] > today[2] ));
        }
    }
}
