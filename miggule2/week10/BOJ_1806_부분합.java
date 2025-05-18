package week10;

import java.util.*;
import java.io.*;

public class BOJ_1806_부분합 {
    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        //배열 입력
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0;
        int right = 0;
        int sum = arr[left]; // sum의 초깃값을 arr[0]을 가짐
        int min = Integer.MAX_VALUE; // 길이 최솟값을 저장할 min 변수

        // 투포인터 풀이 시작
        // 주의할 점 : 왼쪽 포인터를 옮길 때는 값을 빼고 ++, 오른쪽 포인터를 옮길 때는 ++하고 값을 더함
        while (right < n) {
            // 부분합이 k 보다 크거나 같은 경우, 길이 최솟값 갱신
            // 그리고 sum에서 제일 왼쪽 값을 빼고 left 포인터를 옮김.
            if(sum >= k){
                min = Math.min(min, right-left+1);
                sum -= arr[left++];
            }
            // 부분합이 k 보다 작은 경우
            // 오른쪽 포인터를 옮기고 sum에 오른쪽 값 추가
            else {
                if(right == n-1) break; // right 포인터가 끝 값이고, 부분합이 k보다 작을 경우엔 더이상 부분합이 커질 가능성이 없기 때문에 while문 탈출
                else sum += arr[++right];
            }
        }

        // min값이 업데이트 없을 경우 == 부분합이 k 이상이 없는 경우
        if(min == Integer.MAX_VALUE){
            System.out.println(0);
        } else {
            System.out.println(min);
        }
    }
}
