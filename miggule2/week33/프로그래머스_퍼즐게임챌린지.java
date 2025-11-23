package week33;

public class 프로그래머스_퍼즐게임챌린지 {
    public int solution(int[] diffs, int[] times, long limit) {
        int max = 0;

        for(int diff : diffs){
            max = Math.max(max,diff);
        }

        int low = 1;
        int high = max;
        int result = 0;
        while(high > low){
            int mid = (low+high)/2;

            if(isPossible(diffs,times,limit,mid)){
                high = mid;
            } else{
                low = mid+1;
            }

            result = high;
        }

        return result;
    }

    private boolean isPossible(int[] diffs, int[] times, long limit, int level)
    {
        long totalTime = 0;
        long time_prev = 0;
        for(int i = 0; i < diffs.length; i++){

            if(diffs[i] <= level) {totalTime += times[i];}
            else totalTime += (diffs[i]-level)*(time_prev+times[i]) + times[i];

            time_prev = times[i];
        }
        System.out.println(totalTime + " " + level);
        return limit >= totalTime;
    }
}
