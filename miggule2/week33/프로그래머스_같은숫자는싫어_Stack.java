package week33;

import java.util.Deque;
import java.util.LinkedList;
import java.util.Stack;

public class 프로그래머스_같은숫자는싫어_Stack {
    public Stack<Integer> solution(int []arr) {
        Stack<Integer> stack = new Stack<>();

        for(int n : arr){
            if(stack.isEmpty() || stack.peek() != n){
                stack.push(n);
            }
        }

        return stack;
    }
}
