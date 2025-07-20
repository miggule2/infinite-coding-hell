package week21;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class BOJ_10610_30_Greedy {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        Integer[] numArr = new Integer[str.length()];

        int sum = 0;
        boolean isThereZero = false;
        for(int i = 0; i < str.length(); i++){
            numArr[i] = str.charAt(i) - '0';
            if(numArr[i] == 0){isThereZero = true;}
            sum += numArr[i];
        }

        if(sum%3 == 0 && isThereZero){
            Arrays.sort(numArr, Comparator.reverseOrder());
            for(int i = 0; i < numArr.length; i++){
                System.out.print(numArr[i]);
            }
        } else {
            System.out.println(-1);
        }

    }
}
