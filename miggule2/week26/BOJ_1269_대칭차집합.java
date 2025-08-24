package week26;

import java.util.*;
import java.io.*;

public class BOJ_1269_대칭차집합 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray(); // 문제에서 입력 받으라고 배열의 크기를 지정해줬지만 사용하지 않음

        // 이번 문제는 로직보다는 자료구조와 자료구조 조작에 대해서 공부할 수 있는 문제
        String[] array1 = br.readLine().split(" ");
        String[] array2 = br.readLine().split(" ");

        // String 배열은 asList 메서드로 List로 바꿀 수 있음.
        HashSet<String> temp = new HashSet<>(Arrays.asList(array1)); // 차집합 등을 위한 임시 배열 
        HashSet<String> set1 = new HashSet<>(Arrays.asList(array1));
        HashSet<String> set2 = new HashSet<>(Arrays.asList(array2));

        set1.removeAll(set2); // set1-set2
        set2.removeAll(temp); // set2-set1
        set1.addAll(set2); // set1-set2 교집합 set2-set1
        // 반환값은 boolean이기에 조심.

        System.out.println(set1.size());
    }
}
