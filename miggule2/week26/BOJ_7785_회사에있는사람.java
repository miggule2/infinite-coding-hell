package week26;

import java.util.*;
import java.io.*;

public class BOJ_7785_회사에있는사람 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());

        HashSet<String> set = new HashSet<>();
        for(int i = 0; i< n ;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String input = st.nextToken();

            if(input.equals("enter")){
                set.add(name);
            } else {
                set.remove(name);
            }
        }

        List<String> list = new ArrayList<>(set);
        Collections.sort(list,Collections.reverseOrder());

        for(String stay : list){
            bw.write(stay+"\n");
        }

        bw.flush();
        bw.close();
    }
}
