#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{   
	int num;
	cin >> num;
	vector <pair<int, string>> info; //pair로 묶음 설정
	for (int i = 0; i < num; i++)
	{
		string name;
		int cost;
		cin >> name >> cost;
		info.push_back({cost, name});
	}
	sort(info.begin(), info.end(), greater<>()); //내림차순으로 정렬

	int count = 0;
	pair<int, string>  prev = { -1, "" }; // {cost, name}

	for (auto& p : info) {//info동안 반복. index쓰는게 아니라면 auto로 for문 사용.
		if (p.first != prev.first) //현재 cost와 이전 cost가 다르다면
			if (count == 1) { // count==1이면 이름 출력 후 종료
				cout << prev.second;
				return 0;
			}
			else { // count != 1이면 중복되는 값이므로 다시 count = 1, prev 갱신
				count = 1;
				prev = p;
			}
		else {
			count++;
		}
	}
    //예외처리
	if (count == 1) cout << prev.second; 
	else cout << "NONE";
}
