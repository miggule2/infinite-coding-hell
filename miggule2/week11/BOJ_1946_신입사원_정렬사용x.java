package week11;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class BOJ_1946_신입사원_정렬사용x {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        // 배열 입력받기
        for(int i = 0; i < t; i++){
            int n = Integer.parseInt(br.readLine());
            int cnt = 0;

            // 1차 시험 등수를 index로 해서 배열을 입력받으면 1차 시험 성적대로 정렬된 배열을 얻을 수 있음
            int[] arr = new int[n+1];
            for(int j = 1; j <= n; j++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                arr[a] = Integer.parseInt(st.nextToken());
            }

            // 1차 시험 등수대로 정렬된 배열이기에, 배열을 순차적으로 순회하며 이전에 등장한 2차 등수보다 높으면 1차는 못했지만 2차는 더 잘했기에 카운트 할 수 있음.
            // 즉, 1차 시험 등수대로 정렬된 배열을 순회하며 2차 시험은 오름차순이 돼야한다.
            int min = Integer.MAX_VALUE;
            for(int j = 1; j <= n; j++){
                if(min > arr[j]){
                    min = arr[j];
                    cnt++;
                }
            }

            System.out.println(cnt);
        }
    }
}
