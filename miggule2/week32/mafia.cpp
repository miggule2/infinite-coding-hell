#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

// using gemini : Use structures to store member information at once
struct Member{
    string name;
    vector<string> children;
    string parent;
    int descendent_count=0;
    int depth=0;
};

string boss;

// 자손 수를 계산하는 재귀 함수
int calculateDescendent(const string& name, map<string,Member>& members){
    if(members[name].children.empty()) return 0; // 자식이 없는 경우 0
    if(members[name].descendent_count != 0) return members[name].descendent_count; // 자손의 수를 알고 있는 경우 그냥 반환
    int count = 0;

    // 자식을 반환하며 자식들의 자손+1(자식 자신)의 합
    for(string& child : members[name].children){
        count += 1+ calculateDescendent(child,members);
    }

    return members[name].descendent_count = count;
}

// 깊이를 계산하는 재귀함수
int depth(const string& name,map<string,Member>& members){
    if(members[name].depth != 0) return members[name].depth; // 깊이를 이미 알고 있는 경우 반환
    if(name==boss) return 0; // 루트인 경우 0 리턴
    else return members[name].depth = 1 + depth(members[name].parent,members); // 나머지 경우 부모의 깊이+1
}

bool cmp(pair<string,Member>& a, pair<string,Member>& b){
    if(a.second.descendent_count != b.second.descendent_count) return a.second.descendent_count > b.second.descendent_count;
    if(a.second.depth != b.second.depth) return a.second.depth < b.second.depth;
    return a.first < b.first;
}
int main() {
    int n;
    cin >> n;
    set<string> notBoss;
    map<string,Member> members;

    for (int i = 0; i < n-1; i++) {
        string child, parent;

        cin >> child >> parent;
        members[child].name = child;
        members[parent].name = parent;

        members[child].parent = parent;
        members[parent].children.push_back(child);
    }

   // 루트 찾기
    for(auto& [name,member] : members){
        if(member.parent.empty()) {boss = name; break;}
    }

    // 모든 노드 깊이 찾기
    for(auto& [name, member] : members){
        member.depth = depth(name, members);
    }

    // 모든 노드 자손 수 찾기
    for(auto&[name,member] : members){
        member.descendent_count = calculateDescendent(name,members);
    }

    vector<pair<string,Member>> v(members.begin(),members.end());
    sort(v.begin(),v.end(),cmp);

    for(auto& [name,member] : v){
        cout << name << endl;
    }
}