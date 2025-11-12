#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

//all중 hasparent에 포함 안되는 요소 찾기 -> root
string find_root(const set<string>& all, const set<string>& hasparent) {
	for (const string& name : all) {
		if (hasparent.find(name) == hasparent.end()) {
			return name;
		}
	}
}

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

int main()
{
    int n;
    cin >> n;
    map <string, vector<string>> tree;
	//중복제거를 위해 set 사용
    set<string> hasparent;
    set<string> all;

    for (int i = 0; i < n-1; i++) {
        string self, parent;
		cin >> self >> parent;
		tree[parent].push_back(self);
		hasparent.insert(self);
		all.insert(parent);
		all.insert(self);
    }
	string root = find_root(all, hasparent);
	dfs(root, 0, tree);

	vector<string> peopleToSort(all.begin(), all.end());

	//정렬
	sort(peopleToSort.begin(), peopleToSort.end(), [&](const string& a, const string& b) {
		if (personInfo[a].first != personInfo[b].first) { //1순위: descendant 수에 따른 정렬
			return personInfo[a].first > personInfo[b].first;
		}

		if (personInfo[a].second != personInfo[b].second) { //2순위: depth에 따른 정렬
			return personInfo[a].second < personInfo[b].second;
		}

		return a < b; //3순위: 사전순 정렬
		});

	for (const string& person : peopleToSort) {
		cout << person << endl;
	}

}
