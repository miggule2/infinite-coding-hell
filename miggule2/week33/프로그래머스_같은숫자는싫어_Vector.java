package week33;

import java.util.Vector;

public class 프로그래머스_같은숫자는싫어_Vector {
    public int[] solution(int []arr) {
        Vector<Integer> answer = new Vector<>();

        int prev = arr[0];
        answer.add(prev);
        for(int i = 1; i < arr.length; i++){
            if(prev == arr[i]) continue;
            else {
                answer.add(arr[i]);
                prev = arr[i];
            }
        }

        int[] result = new int[answer.size()];
        int i = 0;
        for(int num : answer){
            result[i] = num;
            i++;
        }

        return result;
    }
}
