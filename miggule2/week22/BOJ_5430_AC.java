package week22;

import java.util.*;
import java.io.*;

public class BOJ_5430_AC {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++){
            Deque<String> deque = new LinkedList<>();
            String[] command = br.readLine().split("");
            int j = Integer.parseInt(br.readLine());
            String arrString = br.readLine();
            String[] arr = arrString.substring(1,arrString.length()-1).split(",");
            
            if(j!=0)
            for(String str : arr){
                deque.add(str);
            }

            boolean flag = false;
            boolean isFront = true;
            for(int k = 0; k < command.length; k++){
                if(command[k].equals("R")) {
                    isFront = !isFront;
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
