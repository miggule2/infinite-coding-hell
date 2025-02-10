package week8;

import java.util.*;
import java.io.*;

public class BOJ_2110_공유기설치 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int house = Integer.parseInt(st.nextToken());
        int num = Integer.parseInt(st.nextToken());

        int[] houses = new int[house];
        for(int i = 0; i < house; i++){
            houses[i] = Integer.parseInt(br.readLine());
        }

        //이분 탐색을 위한 정렬
        Arrays.sort(houses);

        // 간격의 최솟값(1) 최댓값(max-min)을 각각 left와 right로 설정
        int left = 1;
        int right = houses[houses.length-1]-houses[0];
        while(left <= right){
            int mid = left + (right - left)/2; // 간격
            int prev = houses[0];
            int count = 1; // 설치 가능한 집의 개수
            for(int i = 1; i < houses.length; i++){
                // 설치된 전집과의 거리가 최소 간격보다 작은 경우 패스 ( 최소 간격이 아니게 돼버림 )
                // 설치된 전집과의 거리가 최소 간격보다 같거나 큰 경우 -> 설치, 설치된 전집을 현재 집으로 설정
                // 최소간격보다 큰 경우에도 같은 일을 하는 이유는 그렇게 해야 최소간격의 케이스가 통과되어 간격이 커져 최소간격이 딱 맞는 경우까지 갈 수 있기 때문
                if(houses[i]-prev >= mid) {
                    count++;
                    prev = houses[i];
                }
            }
            if(count >= num) left = mid + 1;
            else right = mid-1;
        }
        // 될 수 있는 최소 간격중에 최댓값을 구하는 것이기에 right를 출력 ( right는 항상 될 수 있는 값 중에서 최대값을 갖기 때문)
        // left 다음 간격 중 가장 작은 값이기에 left-1 을 해도 동일한 결과 출력
        System.out.println(right);
    }
}
