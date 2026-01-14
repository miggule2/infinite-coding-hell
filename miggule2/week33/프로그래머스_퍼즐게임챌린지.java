package week33;

public class 프로그래머스_퍼즐게임챌린지 {
    public int solution(int[] diffs, int[] times, long limit) {
        int max = 0;

        for(int diff : diffs){
            max = Math.max(max,diff);
        }

        // 가장 작은 level값을 찾ㄱ기 위한 이분 탐색 로직
        int low = 1;
        int high = max;
        int result = 0;
        while(high > low){
            int mid = (low+high)/2; // 중간값

            if(isPossible(diffs,times,limit,mid)){
                high = mid;
            } else{
                low = mid+1;
            }
            result = high;
        }

        return result; // 이분 탐색 후 찾은 최솟값
    }

    // level을 입력 받고 해당 level일 경우 가능한지 판별하는 로직
    private boolean isPossible(int[] diffs, int[] times, long limit, int level)
    {
        long totalTime = 0;
        long time_prev = 0;
        for(int i = 0; i < diffs.length; i++){

            if(diffs[i] <= level) {totalTime += times[i];} // 문제에서 제시한 전체 시간 계산 로직 ( 자신의 레벨보다 쉬운 경우 )
            else totalTime += (diffs[i]-level)*(time_prev+times[i]) + times[i]; // 문제에서 제시한 전체 시간 계산 로직 ( 자신의 레벨보다 어려운 경우 )

            time_prev = times[i];
        }
        System.out.println(totalTime + " " + level);
        return limit >= totalTime;
    }
}
