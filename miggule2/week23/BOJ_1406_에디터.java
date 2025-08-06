package week23;

import java.util.*;
import java.io.*;

public class BOJ_1406_에디터{
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> list = new LinkedList<>();

        String str = br.readLine();
        for(int i = 0; i < str.length(); i++){
            list.add(String.valueOf(str.charAt(i)));
        }
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        ListIterator iter = list.listIterator();
        while(iter.hasNext()){iter.next();}

        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            switch(st.nextToken()){
                case("P") : {
                    String s = st.nextToken();
                    iter.add(s);
                    break;
                }
                case("L") : {
                    if(iter.hasPrevious()) iter.previous();
                    break;
                }
                case("D") : {
                    if(iter.hasNext()) iter.next();
                    break;
                }
                case("B") : {
                    if(iter.hasPrevious()){
                        iter.previous();
                        iter.remove();
                    }
                    break;
                }
                default : break;
            }
        }
        System.out.println(String.join("",list));
    }
}
