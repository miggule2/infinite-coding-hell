package week12;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.HashMap;

public class BOJ_18870_좌표압축 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] array = new int[n];
        for(int i = 0; i < n; i++){
            array[i] = Integer.parseInt(st.nextToken());
        }

        int[] sortedArray = array.clone();
        Arrays.sort(sortedArray);
        HashMap<Integer,Integer> map = new HashMap<>();
        int index = 0;
        int prev = sortedArray[0];
        for(int i = 0; i < sortedArray.length; i++){
            if(prev != sortedArray[i]) {index++;}

            map.put(sortedArray[i],index);
            prev = sortedArray[i];
        }

        for(int i = 0; i < array.length; i++){
            array[i] = map.get(array[i]);
        }
        for (int i : array) {
            bw.write(Integer.toString(i)); bw.write(" ");
        }

        bw.flush();
        bw.close();
    }
}
