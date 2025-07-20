## 해결법
### 1. 그리디
* 이 문제는 회의를 많이 하는게 포인트이기 때문에, ```끝나는 시간```을 기준으로 풀어야 한다.
* 조금 더 디테일하게 말하면 
  1. __```[시작 시간, 마치는 시간]```를 ```ArrayList<int[]>```에 대입__
  ```java
    LinkedList<int[]> list = new LinkedList<>();
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            list.add(new int[]{a,b});
        }
  ```
  2. ```끝나는 시간(같으면 시작 시간)```으로 정렬
    ```java
    list.sort((a,b)->{
        if(a[1]==b[1]){return Integer.compare(a[0],b[0]);}
        else return Integer.compare(a[1],b[1]);
    });
    ```
  3. 제일 작은 ```끝나는 시간```으로 ArrayList 원소를 읽어나가며 __시작시간이 ```제일 작은 끝나는 시간```보다 큰 경우__ 끝나는 시간 업데이트
     * 이미 ```끝나는 시간```기준으로 정렬된 리스트이기 때문에, ```시작시간이 제일 작은 끝나는 시간보다 큰 경우``` 이 문장의 뜻은 ```제일 일찍 끝나는 회의 다음으로 일찍 끝나는 회의를 찾은 경우```로 해석됨.

    ```java
    int endtime = 0;
    int count = 0;
    for (int[] ints : list) {
        if(ints[0] >= endtime){
        endtime = ints[1];
        count++;
        }
    }
    ```
  4. 위 과정을 반복
#### 시행착오
1. 문제 풀이 방법은 같으나 배열,HashMap을 사용해서 풀이했을 때 메모리 초과 발생
    * 입력받는 수의 최댓값(TMAX)가 너무 커서 메모리 초과 발생한 것으로 예상
2. ArrayList<int[]> 정렬 시 문제
   * 처음 코드는 ```list.sort(Comparator.comparingInt(a -> a[1]));``` 이렇게 작성하여, ```시작시간```에 대한 정렬이 이루어지지 않았음
   * 하지만 람다를 이용해서 ```끝나는 시간이 같을 경우 시작시간으로 정렬을 시행```
#### 전체 코드
```java
public class BOJ_1931_회의실배정 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n =  Integer.parseInt(br.readLine());

        StringTokenizer st;
        LinkedList<int[]> list = new LinkedList<>();
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            list.add(new int[]{a,b});
        }

        list.sort((a,b)->{
            if(a[1]==b[1]){return Integer.compare(a[0],b[0]);}
            else return Integer.compare(a[1],b[1]);
        });

        int endtime = 0;
        int count = 0;
        for (int[] ints : list) {
            if(ints[0] >= endtime){
                endtime = ints[1];
                count++;
            }
        }

        System.out.println(count);
    }
}
```