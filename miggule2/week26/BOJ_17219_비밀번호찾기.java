package week26;

import java.util.*;
import java.io.*;

public class BOJ_17219_비밀번호찾기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] num = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = num[0];
        int m = num[1];

        HashMap<String,String> map = new HashMap<>();
        for(int i = 0; i < n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            map.put(st.nextToken(),st.nextToken());
        }

        for(int i = 0;i<m;i++){
            bw.write(map.get(br.readLine())+"\n");
        }
        bw.flush();
        bw.close();
    }
}
