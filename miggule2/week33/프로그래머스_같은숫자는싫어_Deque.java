package week33;

import java.util.Deque;
import java.util.LinkedList;

public class 프로그래머스_같은숫자는싫어_Deque {
    public int[] solution(int []arr) {
        Deque<Integer> deque = new LinkedList<>();

        for(int n : arr){
            if(deque.isEmpty() || deque.getLast() != n){
                deque.addLast(n);
            }
        }

        int[] result = new int[deque.size()];
        for(int i = 0; i< result.length;i++){
            result[i] = deque.getFirst();
            deque.removeFirst();
        }

        return result;
    }
}
