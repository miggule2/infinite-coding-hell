### [programmers] / pccp_기출_동영상재생기 / LV1 / 40분

- 문자열로 입력된 시간을 coomand에 따라 변경해야되는 문제
- 시간이기 때문에 60초 단위로 분/초를 모두 신경쓰는건 복잡하기 때문에 문자열 시간을 모두 초 단위의 int형으로 변환하는 함수 작성
- 주어진 모든 문자열 시간에 대해 to_sec()함수 적용
- 오프닝 시간에 포함되면 오프닝 종료시점으로 이동
- min, max함수를 통해 시작이나 종료 10초 이내에 command적용시, 시작/종료시점으로 이동되게 코드 작성
''' 
f'{(pos//60):02}:{(pos%60):02}' '''
- 출력 형태에 맞게 10진수의 2자리수로 출력

### [programmers] / pccp기출_붕대감기 / LV1 / 1시간

- 공격에 따른 체력감소, 체력회복, 연속체력회복 달성시 추가체력회복을 구현해야하는 문제
- 처음에는 마지막공격시점을 종료시점으로 하여 그때까지의 모든 시간을 for문을 통해 돌리려 하였지만 시간을 더 적게 사용할 수 있는 방법을 찾아봄
- 주어진 공격시점들만 for문을 통해 돌리면 공격 사이시간은 체력회복이 이루어지기 때문에 이를 통해 코드 실행시간 감소
- 마지막 공격 이후에는 체력회복이 이루어지지 않기 때문에 마지막 공격 직전까지만 for문 실행
- for문 실행시 공격으로 인한 체력감소부터 한 뒤, 다음 공격 전까지의 체력회복을 하도록 코드 작성
- sub_time//bandage[0]를 통해 연속 체력회복시 추가체력 회복을 구현

### 자료구조 과제 / mafia / 2시간

- 트리 관련 문제로 처음에는 수업시간에서처럼 node를 만들어 tree를 직접 구현하려 했지만 tree탐색만 이루어지면 될것같아 dfs방향으로 생각함.
- 주어진 입력은 자신과 부모노드에 대한 정보만 주기 때문에 이를 종합하여 value값을 자식들로 가지는 map을 만듦.
- root를 찾기 위해 set을 이용하여 모든 사람들이 있는 set에서 child가 있는 set에 포함되지 않는 노드를 찾음.
'''
map<string, pair<int, int>> personInfo; //<name, <descendant 수, depth>>
int dfs(const string& name, int d, map <string, vector<string>>& tree) {
	personInfo[name].second = d; //depth저장
	int descendant = 0;
	if (tree.count(name)) {
		for (const string& child : tree[name]) {
			descendant += 1 + dfs(child, d + 1, tree); //재귀를 통해 dfs탐색으로 각 노드별 자손수와 depth구하기
		}
	}
	personInfo[name].first = descendant;
	return descendant; 
}
'''
- 재귀를 통해 구현한 dfs를 사용하여 root부터 탐색하면서 각 노드가 가지는 descendant수와 depth를 pair로 가지는 map을 추가로 생성.
- sort를 통해 자손수, depth, 사전순정렬을 기준으로 정렬 후, vector에 저장함.
