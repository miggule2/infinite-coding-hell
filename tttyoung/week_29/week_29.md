### 자료구조 과제 / coin / 2시간 반

- 방대한 양의 데이터에서 특정 구간의 최대,최솟값을 구하는 문제.
- 단순히 for문을 사용하면 주어진 데이터가 200만개가 넘기 때문에 시간초과 발생 ->세그먼트 트리 사용
- txt파일의 데이터를 입력으로 받아서 벡터에 저장하여 사용함.
```
        vector<num> data;
        ifstream fin("Pitcoin.txt");
        int N; //입력개수
        fin >> N;
        data.reserve(N); //vector에 공간 미리 할당
        num line_data;
        while (fin >> line_data.time_val >> line_data.coin_value) {
            data.emplace_back(line_data);
        }
```

- 세그먼트 트리 뼈대를 만들고 build함수를 이용해 세그먼트 트리에 값 채우기, query를 이용해 특정 구간내 최대 최솟값 찾는 방식으로 코드를 나눔.
- build함수와 query함수 모두 좌측 우측 구간을 나누어 재귀를 통해 값을 구함. 
- build에서는 재귀를 통해 각 tree node에 min, max value를 struct로 저장함.
- query에서는 구간을 더 나눌 수 없을때까지 재귀를 통해 좌측구간 결과값, 우측구간결과값을 구한 후, 이를 min max함수를 사용해 최종 결과값을 구함.
- txt파일의 입력이 시간으로 들어오기 때문에 만약 310-320 구간의 최대최소를 찾지만 310이 없으면 이보다 작은 시간중 최대인 시간의 값과 동일시 해야하기 때문에 make_index함수를 구현.
- upper_bound를 이용해 해당 시간의 index를 구함.

### 자료구조 과제 / lab_grade / 2시간

- 입력 기준이 주어져있으며 점수를 기준별 점수로 바꾼 후 주어진 기준순서에 따라 정렬하는 문제
- 모든 기준은 0을 포함하지 않는 기준들이므로 처음에는 모든 입력을 받아 저장한 후, 0을 제외하는 방식을 생각했으나 입력을 받을때부터 0이면 사용하지 않는 방식을 조언받음.
- make_standard함수를 구현하여 원점수 벡터(0이 없는)가 parameter로 들어왔을때 기준별 점수벡터를 반환함.
- sort함수에 람다를 사용하여 원하는 기준대로 정렬할 수 있도록 함.
- for문을 사용하여 기준 순서를 돌면서 해당 기준의 점수별로 정렬을 함.
- 만약 모든 정렬이후에도 점수가 같으면 사전순 이름을 출력하도록 마지막에 for문 밖에 `return a.name<b.name`를 해줌.
```
    sort(students.begin(), students.end(), [&](const Student& a, const Student& b) {
        for (int i = 0; i < 5; i++) { //for문을 돌리면서 정렬기준을 계속 넘김
            if (a.sorting_standard[sorting[i] - 1] != b.sorting_standard[sorting[i] - 1])
                return a.sorting_standard[sorting[i] - 1] > b.sorting_standard[sorting[i] - 1];
        }
        return a.name < b.name;
        });
```

### [boj] / 10814_나이순정렬 / 실버5 / 20분

- 정렬 연습을 위해 간단한 정렬문제를 풀어봄.
- 나이순으로 오름차순 정렬하며 만약 나이가 같다면 먼저 입력된 순서로 출력해야하는 문제.
- lab_grade와 같이 sort에 람다를 사용하여 조건을 걸어주는 방식으로 풀어보았지만 틀렸음.
- sort함수는 주어진 배열의 순서를 보장하지 않지만 stable_sort는 주어진 배열 순서를 보장해줌.
```
    stable_sort(people.begin(), people.end(), [&](const person& a, const person& b) { //stable_sort로 정렬순서 지킴
        return a.age < b.age; //나이순서로 정렬
        });
```
