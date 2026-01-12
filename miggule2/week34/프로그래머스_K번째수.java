package week34;

import java.util.Arrays;

public class 프로그래머스_K번째수 {
    public int[] solution(int[] array, int[][] commands) {
        int[] result = new int[commands.length];

        int index = 0;
        for(int[] command : commands){
            int[] arr = new int[command[1]-command[0]+1];

            for(int i = 0; i < arr.length; i++){
                arr[i] = array[command[0]-1+i];
            }

            Arrays.sort(arr);

            result[index] = arr[command[2]-1];
            index++;
        }

        return result;
    }
}
