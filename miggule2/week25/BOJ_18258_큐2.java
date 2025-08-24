package week25;

import java.util.*;
import java.io.*;

public class BOJ_18258_큐2 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());

        LinkedList<Integer> queue = new LinkedList<>();
        int size = 0;

        for(int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            switch(st.nextToken()){
                case "push" :
                    int num = Integer.parseInt(st.nextToken());
                    queue.addFirst(num);
                    size++;
                    break;

                case "pop" :
                    if(size == 0){
                        bw.write(-1+"\n");
                        break;
                    }
                    size--;
                    bw.write(queue.removeLast()+"\n");
                    break;

                case "size" :
                    bw.write(size+"\n");
                    break;

                case "empty" :
                    if(size == 0) bw.write(1+"\n");
                    else bw.write(0+"\n");
                    break;

                case "front" :
                    if(size == 0) bw.write(-1+"\n");
                    else bw.write(queue.getLast()+"\n");
                    break;

                case "back" :
                    if(size == 0) bw.write(-1+"\n");
                    else bw.write(queue.getFirst()+"\n");
                    break;
                default : break;
            }
        }

        bw.flush();
        bw.close();
    }
}
