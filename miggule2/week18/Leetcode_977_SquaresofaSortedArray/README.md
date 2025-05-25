## 해결법
### 1. 값들을 절댓값으로 변경 후, sorting
* 가장 기본적인 코드
#### 코드
```java
public int[] sortedSquares(int[] nums) {
    for(int i = 0; i < nums.length; i++){
        nums[i] = (int)Math.pow(nums[i],2);
    }

    Arrays.sort(nums);
    return nums;
}
```

### 2. 투포인터 사용
* 문제 조건에 값들이 오름차순으로 제공된다는 조건을 이용.
* 새로운 배열을 만들어 제곱값들을 저장해서 새로운 배열을 리턴.
* 투포인터를 양 끝에 배치해서 절댓값을 비교하여 큰 값을 제곱해서 배열의 제일 오른쪽 칸부터 채워 내려옴.
* 양 포인터 사이에 있는 값들은 포인터에 있는 더 큰 값보다는 무조건 작을 수 밖에 없음을 이용.

#### 코드
```java
public int[] sortedSquares(int[] nums) {
    int[] result = new int[nums.length];
    int left = 0;
    int right = nums.length-1;

    for(int i = nums.length-1; i >= 0; i--){
        if(Math.abs(nums[left]) > Math.abs(nums[right])){
            result[i] = (int)Math.pow(nums[left++],2);
        } else{
            result[i] = (int)Math.pow(nums[right--],2);
        }
    }

    return result;
}
```