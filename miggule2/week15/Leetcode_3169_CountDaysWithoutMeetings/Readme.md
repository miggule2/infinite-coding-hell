## 해결법
### 1. Simple Logic
* 모든 meeting 날짜를 순회하여 표시하고, 모든 days를 순회하며 meeting이 없는 날짜를 세는 방법(완전 탐색)은 최악의 경우 ```O(n^2)```의 시간복잡도가 나옴.
* 그래서 시작과 끝만 표시를 하고 셀 때만 조금의 처리만 해주면 되는 풀이가 존재한다.
1. 시작, 끝 점을 표시할 map 생성
2. meetings를 순회하며 map에다 시작에는 +1, 끝에는 -1 하는 것을 반복한다.
3. 그렇게 해서 처음부터 쭉 순회하며 key값을 더해 나가면 __현재 진행중인 미팅이 있으면 ```onMeeting>0``` 일 거고, 없으면 ```onMeeting==0```을 만족할 것이다. 
4. 그래서 onMeeting이 0일 때의 day 숫자만 세어주면 문제 해결.
5. 하지만 모두 순회할 필요가 없는데, 이는 onMeeting이 바뀌는 경계(map의 key값)만 생각해주면 되기 때문이다.
6. onMeeting이 0일 때, ```현재 key - 이전 key - 1```를 해주면 result를 구할 수 있음.

* __코드__
```java
class Solution {
    public int countDays(int days, int[][] meetings) {
        TreeMap<Integer,Integer> map = new TreeMap<>(); // key값을 이용한 순회를 위해선 key값이 오름차순으로 정렬돼야 하기에 TreeMap 사용
        for(int[] meeting : meetings){
            map.put(meeting[0],map.getOrDefault(meeting[0],0)+1);
            map.put(meeting[1],map.getOrDefault(meeting[1],0)-1);
        }
        int pre = 0; // 이전 키값 저장
        int onMeeting = 0; // 현재 진행되고 있는 미팅 개수
        int result = 0; 
        for(int key : map.keySet()){
            if(onMeeting == 0) {
                result += key-pre-1; // 현재 미팅이 없는 경우 이전 키값 ~ 현재 키값 사이 날들엔 미팅이 없는 날들
            }

            onMeeting += map.get(key);

            pre = key;
        }

        result += days-pre; // 마지막 키값 ~ 끝까진 미팅 없음.

        return result;
    }
}
```

* __시간복잡도__ : ```O(nlogn)``` (__TreeMap이 red-black tree 구조 사용__)

### 2. sorting
* 위의 방법은 시작과 끝을 저장할 별도의 자료구조가 필요했음.
* 하지만 meeting 시작 날짜를 기준으로 정렬하면 추가 자료구조 없이 문제를 해결할 수 있음.
1. 각 meeting의 처음 요소(미팅 시작 날짜)를 기준으로 정렬.
2. meeting을 순회하며 이전에 등장한 end의 최대값+1보다 start가 큰 경우(현재 진행중인 미팅이 없는 경우)에 ```start-maxEnd-1```만큼을 result에 더해준다.

* __코드__
```java
class Solution {
    public int countDays(int days, int[][] meetings) {
        Arrays.sort(meetings,Comparator.comparingInt((int[] o) -> o[0])); // 각 meeting의 시작날을 기준으로 sort

        int maxEnd = 0;
        int result = 0;

        for(int[] meeting : meetings){
            int start = meeting[0];
            int end = meeting[1];
            
            // 이전에 등장한 maxEnd+1보다 start가 큰경우는 현재 진행중인 미팅이 없다는 의미
            if(start > maxEnd+1){
                result += start-maxEnd-1; // 이전 미팅 끝난 날짜 ~ 이번 미팅 시작 날짜 사이 동안엔 미팅이 없기에 더해주기
            }

            maxEnd = Math.max(maxEnd,end);
        }
        result += days - maxEnd; // 마지막 미팅 ~ 끝까지는 미팅이 없기에 더해주기

        return result;
    }
}
```
* __시간복잡도__ : ```O(nlogn)``` (sort)