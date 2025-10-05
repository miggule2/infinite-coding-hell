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

struct University{
    int totalCote=0;
    set<Student> students;
};

class GradeSystem{
public:
    int limit;
    GradeSystem(int _limit) : limit(_limit) {}
    map<string, University> universityMap;
    void insertStudent(string &universityName, int id, int cote);
    void popStudent(int start, int end);
};

void GradeSystem::insertStudent(string& universityName, int id, int cote) {
    universityMap[universityName].totalCote += cote;
    universityMap[universityName].students.insert(Student(id,cote));
}

void GradeSystem::popStudent(int start, int end) {
    vector<pair<string,University>> tempVec;
    for(auto& pair : universityMap){
        if(pair.second.students.size() >= limit) tempVec.push_back(pair);
    }

    sort(tempVec.begin(), tempVec.end(), [](pair<string,University>& a, pair<string,University>& b){
        if(a.second.students.size() == b.second.students.size()) return a.second.totalCote > b.second.totalCote;
        else return a.second.students.size() > b.second.students.size();
    });

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