package week33;

public class 프로그래머스_최댓값과최솟값 {
    public String solution(String s) {
        String[] stringArr = s.split(" ");

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for(String str: stringArr){
            int n = Integer.parseInt(str);
            min = Math.min(min,n);
            max = Math.max(max,n);
        }

        return min + " " + max;
    }
}
