package week_16;
import java.util.*;

public class BOJ_2588_곱셈 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int B1 = B % 10;
        int B2 = (B / 10) % 10;
        int B3 = B / 100;
        System.out.println(A * B1);
        System.out.println(A * B2);
        System.out.println(A * B3);
        System.out.println(A * B);
        sc.close();
    }
}
