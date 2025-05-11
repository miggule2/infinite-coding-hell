## 해결법
### 1. 제출 풀이
1. ```nums``` 배열에 등장하는 숫자를 index로 하고, 등장횟수를 value로 하는 배열 생성.
2. 그 배열을 순회하며 홀수인 경우(짝이 맞지 않는 경우)가 나오면 ```false```, 아니면 ```true``` 반환

* __코드__
```java
class Solution {
    public boolean divideArray(int[] nums) {
        int[] array = new int[500+1];

        for(int num : nums){
            array[num]++;
        }

        boolean result = true;
        
        for(int count : array){
            if(count % 2 == 1) {result = false; break;}
        }

        return result;
    }
}
```

* __시간복잡도__ : ```O(n)```

### 2. Sorting
* 이 풀이법은 일단 nums를 정렬한 후, 처음부터 2개씩 건너뛰며 순회하여 __다음 요소가 현재 요소와 다른 경우(짝이 없는 경우)__ false를 반환.
     
 
* __코드__
```java
public class Leetcode_2206_DivideArrayIntoEqualPairs_Sorting {
    class Solution {
        public boolean divideArray(int[] nums) {
            Arrays.sort(nums);

            boolean result = true;
            for(int i = 0; i < nums.length; i += 2){
                if(nums[i] != nums[i+1]){
                    result = false;
                    break;
                }
            }

            return result;
        }
    }
}
```

* __시간복잡도__ : ```O(nlogn)``` (배열 sorting의 시간복잡도)

### 3. Boolean Array
* 내가 처음 제출했던 풀이와 비슷한 방법.
* 각 숫자를 index로 하는 boolean 배열을 만들어, ```nums```를 순회하며 각 index의 boolean 값을 flip.
* 순회가 끝난 후에는 각 index의 값이 짝이 있는 경우는 ```false``` 없는 경우는 ```true``` 가 됨.
* 그래서 boolean 배열을 순회하며 결과 반환
  

* __코드__
```java
public class Leetcode_2206_DivideArrayIntoEqualPairs_BooleanArray {
    class Solution {
        public boolean divideArray(int[] nums) {
            int max = Integer.MIN_VALUE;
            for(int num : nums){
                max = Math.max(max,num);
            }

            boolean[] boolArr = new boolean[max+1];

            for(int num : nums){
                boolArr[num] = !boolArr[num];
            }

            for(boolean bool : boolArr){
                if(bool) return false;
            }

            return true;
        }
    }
}
```

* __시간복잡도__ : ```O(n)```

### 4. HashSet
* 이 방법은 ```HashSet```을 이용하는 방법.
* nums를 순회하며 set안에 있는 경우 remove, 없는 경우 add한다.
* 그러면 배열이 끝난 후 __홀수 번 나온 수(짝이 없는 경우)가 있으면 set에 숫자가 남음.__    
 

* __코드__
```java
public class Leetcode_2206_DivideArrayIntoEqualParis_HashSet {
    class Solution {
        public boolean divideArray(int[] nums) {
            HashSet<Integer> set = new HashSet<>();

            for(int num : nums){
                if(set.contains(num)) set.remove(num);
                else set.add(num);
            }

            return set.isEmpty();
        }
    }
}
```

* __시간복잡도__ : ```O(n)```

### 5. HashMap
* 첫번째와 유사한 풀이법이다.
* 하지만 이 풀이법에서는 배열 대신 ```HashMap```을 사용해서 풀이.
* 전체적인 풀이는 똑같고 HashMap의 key에는 숫자, value에는 나온 횟수를 저장한다는 점만 다름.    
  

* __코드__
```java
public class Leetcode_2206_DivideArrayIntoEqualParis_HashMap {
    class Solution {
        public boolean divideArray(int[] nums) {
            HashMap<Integer,Integer> countMap = new HashMap<>();

            for(int num : nums){
                countMap.put(num,countMap.getOrDefault(num,0)+1);
            }

            for(int num : countMap.keySet()){
                if(countMap.get(num) % 2 == 1) return false;
            }
            return true;
        }
    }
}
```

* __시간복잡도__ : ```O(n)```