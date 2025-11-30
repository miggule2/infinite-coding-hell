package week34;

public class 프로그래머스_타겟넘버 {
    public static int result = 0;
    public int solution(int[] numbers, int target) {
        dfs(numbers,0,0,target);
        return result;
    }

    // dfs 로직
    // 전달받은 index가 numbers의 길이-1 (즉, 마지막 인덱스)일 경우에는 마지막 인덱스의 요소 +,- 한 결과와 비교하여 target과 일치하면 ++
    // 그 외의 index의 경우엔 index는 index+1, sum은 sum +- numbers[index]해서 다음 단계에 앞선 합 정보를 넘김
    private void dfs(int[] numbers, int index, int sum, int target){
        if(index == numbers.length-1){
            if(sum+numbers[index] == target || sum-numbers[index] == target) result++;
            return;
        }

        dfs(numbers,index+1,sum+numbers[index],target);
        dfs(numbers,index+1,sum-numbers[index],target);
    }
}
