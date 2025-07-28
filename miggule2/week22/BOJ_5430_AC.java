package week22;

import java.util.*;
import java.io.*;

public class BOJ_5430_AC {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++){
            //입력
            Deque<String> deque = new LinkedList<>();
            String[] command = br.readLine().split("");
            int j = Integer.parseInt(br.readLine());
            String arrString = br.readLine();
            String[] arr = arrString.substring(1,arrString.length()-1).split(",");
            
            if(j!=0)
            for(String str : arr){
                deque.add(str);
            }
            
            //로직
            // 1. R의 경우엔 데크 앞뒤만 바꿔서 poll을 진행하면 실제로 뒤집기를 시행하지 않아도 됨.
            // 2. D의 경우 현재 뒤집기(isFront)의 상태에 따라
                // 뒤집기가 안 된 상황 : pollFirst() 시행
                // 뒤집기가 된 상황 : pollLast() 시행
            boolean flag = false; // error 출력을 위한 flag변수
            boolean isFront = true; // 뒤집기를 처리하기 위한 변수
            for(int k = 0; k < command.length; k++){
                if(command[k].equals("R")) {
                    isFront = !isFront; // 뒤집기
                }

                else {
                    if(deque.isEmpty()) {
                        flag = true;
                        break;
                    } else {
                        if(isFront) deque.pollFirst();
                        else deque.pollLast();
                    }
                }
            }
            // 출력
            if(flag) {bw.write("error\n");}
            else {
                bw.write("[");
                int size = deque.size();
                if(isFront) {
                    for(int k = 0; k < size; k++){
                        bw.write(deque.pollFirst());
                        if(k != size-1) bw.write(",");
                    }
                } else {
                    for(int k = 0; k < size; k++){
                        bw.write(deque.pollLast());
                        if(k != size-1) bw.write(",");
                    }
                }
                bw.write("]");
                bw.write("\n");
            }
        }
        bw.flush();
        bw.close();
    }
}
