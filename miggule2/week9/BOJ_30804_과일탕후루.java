package week9;

import java.io.*;
import java.util.*;

public class BOJ_30804_과일탕후루 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] array = new int[n];
        for(int i = 0; i < n; i++){
            array[i] = Integer.parseInt(st.nextToken());
        }

        // 현재 카운트하고 있는 과일
        // [0]은 먼저 나온 과일, [1]은 뒤에 나온 과일
        int[] fruits = new int[2];
        fruits[0] = array[0];
        int start = 0; // 왼쪽 포인터
        int end = 0; // 오른쪽 포인터
        int max = 0; // result
        int temp = 0; // 과일 두개를 카운터 하고 있는 경우 다음 새로운 과일이 들어왔을 떄, 다음 시작점을 찾기 위해 두 과일 중 뒤에 나오는 과일의 시작점 저장
        // 두번째 과일이 나올 때까지 탐색
        for(int i = 1; i < n; i++){
            if(array[i] != fruits[0]) {
                fruits[1] = array[i];
                end = temp = i;
                max = end-start+1;
                break;
            }
        }

        // 투포인터 풀이
        // 배열 순회하며 각 케이스마다의 진행
        // 1. fruits[1]과 같은 경우(바로 전 과일과 동일한 경우) : end pointer ++;
        // 2. fruits[0]과 같은 경우(과일 전체 개수는 2개지만 바로 전 과일과는 다른 경우) : end pointer++, fruits 순서 바꾸기, temp를 현재 과일의 위치로 바꿔주기
        // 3. fruits엔 없는 새로운 과일이 나온 경우 : 최대 길이 갱신, start를 temp로, end++, temp를 end로, fruits[0]을 기존 마지막 과일, fruits[1]을 새로운 과일로.
        for(int i = end+1; i< n; i++){
            if(array[i] == fruits[1]) { end++; }
            else if(array[i] == fruits[0]) { end++; temp = end; }
            else {
                max = Math.max(max,end-start+1);
                start = temp;
                end++;
                temp = end;
                fruits[0] = array[start];
                fruits[1] = array[end];
            }
        }
        max = Math.max(max,end-start+1); // 마지막엔 끝이기 때문에 최대 길이 갱신

        System.out.println(max);
    }
}
