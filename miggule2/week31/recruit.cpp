#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

// using gemini : I tried to process it using pair, but the code was not intuitive, so I used a structure.
struct Student{
    int id;
    int cote;

    Student(int _id, int _cote) : id(_id), cote(_cote){}
    bool operator < (const Student& other) const{
        if(cote == other.cote) return id > other.id;
        else return cote > other.cote;
    }
};

// 대학별로 학생 정보를 저장할 구조체
struct University{
    int totalCote=0;
    set<Student> students;
};

// 핵심 로직
class GradeSystem{
public:
    int limit;
    GradeSystem(int _limit) : limit(_limit) {}
    map<string, University> universityMap;
    void insertStudent(string &universityName, int id, int cote);
    void popStudent(int start, int end);
};

// 대학별 cote합 / 학생들 set insert
// set에 자료를 넣을 때 자동으로 sort를 하며 트리형태로 넣게되는데 그 과정을 위해 학생 구조체에 "<" operator 오버로딩
void GradeSystem::insertStudent(string& universityName, int id, int cote) {
    universityMap[universityName].totalCote += cote;
    universityMap[universityName].students.insert(Student(id,cote));
}

// 제일 구현하기 어려웠던 로직
void GradeSystem::popStudent(int start, int end) {
    vector<pair<string,University>> tempVec; // map 정렬을 위한 vec
    for(auto& pair : universityMap){
        if(pair.second.students.size() >= limit) tempVec.push_back(pair); // limit보다 많은 대학들만 선별
    }

    // 학생수, cote 총 합 순으로 내림차순 정렬
    sort(tempVec.begin(), tempVec.end(), [](pair<string,University>& a, pair<string,University>& b){
        if(a.second.students.size() == b.second.students.size()) return a.second.totalCote > b.second.totalCote;
        else return a.second.students.size() > b.second.students.size();
    });

    // 각 대학별 1등, 2등 이런식으로 상위 대학부터 내려오며 ranking 저장
    vector<pair<string,Student>> ranking;
    int level = 0;
    while(true){
        bool isAdded = false;
        for(auto& keyValue : tempVec){
            if(keyValue.second.students.size() > level) {
                auto it = keyValue.second.students.begin();
                advance(it,level); // set is not allowed indexing
                ranking.push_back({keyValue.first,*it});
                isAdded = true;
            }
        }
        level++;
        if(!isAdded) break;
    }

    // 요청받은 순위만 출력 & set에서 pop
    int size = ranking.size();
    for(int i = 0; i < size;i++){
        if(i >= start-1 && i <= end-1) {
            cout << ranking[i].second.id << " ";
            universityMap[ranking[i].first].students.erase(ranking[i].second);
            universityMap[ranking[i].first].totalCote -= ranking[i].second.cote;
        }
    }
    cout << endl;
}

int main(){
    int n, k;
    cin >> n >> k;

    GradeSystem* gradeSystem = new GradeSystem(k);

    for(int i = 0; i < n; i++){
        string s;
        cin >> s;
        if(s == "POP"){
            int start, end;
            cin >> start >> end;
            gradeSystem->popStudent(start,end);

        } else{
            int id, cote;
            cin >> id >> cote;
            gradeSystem->insertStudent(s,id,cote);
        }
    }

    delete gradeSystem;
}