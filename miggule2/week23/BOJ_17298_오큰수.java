package week23;

import java.util.*;
import java.io.*;

public class BOJ_17298_오큰수 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 입력도구
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)); // 출력도구
        int n = Integer.parseInt(br.readLine());

        String[] numStrArr = br.readLine().split(" "); // 처음 배열 저장
        Stack<int[]> stack = new Stack<>(); // 로직 처리를 위한 스택 (처음 배열의 위치를 저장하기 위해 (배열,인덱스)를 저장)
        int[] result = new int[n]; // 결과 배열
        int prev = Integer.MAX_VALUE;

        // 로직 시작
        // 1. 입력 받은 수가 이전보다 작은 경우(내림차순) : 그냥 스택에 푸시
        // 2. 입력 받은 수가 이전보다 큰 경우(오름차순) : 오른쪽에 큰 수가 등장했고, 지금 스택에는 내림차순으로 정렬된 상태이기에 현재 수보다 큰 수가 나올때까지 팝(팝된 수의 오큰수는 현재 숫자가 됨)
        // 3. 2의 과정이 끝난 후 현재 수를 스택에 푸시
        // 4. 위의 과정을 처음 배열의 수만큼 반복
        // 5. 4번까지 끝낸 후 스택에 남아있는 수가 오큰수가 없는 상태기에 모두 -1로 처리                           
        for(int i = 0; i < n ; i++){
            int k = Integer.parseInt(numStrArr[i]);
            if(k < prev) stack.push(new int[]{k,i}); // 내림차순
            // 오름차순
            else {
                // 오큰수가 없을 떄까지 반복
                while(!stack.isEmpty() && stack.peek()[0] < k){
                    result[stack.pop()[1]] = k;
                }
                stack.push(new int[]{k,i});
            }
            prev = k;
        }
        
        // 오큰수가 없는 수 처리
        while(!stack.isEmpty()){
            result[stack.pop()[1]] = -1;
        }
        
        // System.out.println 으로 했을 떄 시간초과가 발생하여 변경
        for(int num : result){
            bw.write(num+" ");
        }
        
        bw.flush();
        bw.close();
    }
}
