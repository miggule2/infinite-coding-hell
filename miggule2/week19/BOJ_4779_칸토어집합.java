package week19;

import java.util.*;
import java.io.*;

public class BOJ_4779_칸토어집합 {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while((line=br.readLine())!=null){
            int n = Integer.parseInt(line);
            if(n==0) {System.out.println("-"); continue;}
            int now = (int)Math.pow(3,n);

            String[] arr = new String[now]; // 길이가 3^n인 문자열 배열 생성
            Arrays.fill(arr, " "); // 배열에 빈문자열 대입
            divide(arr,0,now-1,now); // 분할정복 시작
            System.out.println(String.join("", arr));
        }
    }

    // 배열의 시작점, 끝점, 길이를 전달하여 배열상의 문자열을 갈아 끼우기 위한 지점을 넘겨주는 식
    private static void divide(String[] arr, int start, int end, int len){
        if(len==3) { arr[start] = "-"; arr[end] = "-";} // 길이가 3^1 인 배열의 경우 처음과 끝에 "-" 문자열 대입 후 재귀 중단
        else{
            // 배열을 3등분으로 나누기
            // 처음과 끝에만 재귀 진행(중간에는 빈문자열만 남아있도록 하기 위함)
            int nextLen = len/3;
            divide(arr,start,start+nextLen-1,nextLen);
            divide(arr,start+2*nextLen,end,nextLen);
        }
    }
}
