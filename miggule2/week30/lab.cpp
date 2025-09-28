#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> priority;

struct Student {
    string name;
    vector<int> score;
};

int main(){
    int n, k;
    cin >> n >> k;

    for(int i = 0; i  < 5; i++){
        int index;
        cin >> index;
        priority.push_back(index-1);
    }

    vector<Student> students;
    for(int i = 0; i < n; i++){
        string name;
        cin >> name;
        int attendance = 0, sum = 0, minScore = 100, maxScore = 0, hundredScore = 0;
        for(int j = 0; j < k; j++){
            int num;
            cin >> num;

            if(num == 0) continue;

            attendance++;
            sum += num;
            minScore = min(minScore,num);
            maxScore = max(maxScore,num);
            if(num == 100) hundredScore++;
        }
        students.push_back({name,{attendance,sum,minScore,maxScore,hundredScore}});
    }

    sort(students.begin(), students.end(),[](const Student& a, const Student& b){
        for(int i = 0; i < 5; i++){
            if(a.score[priority[i]] != b.score[priority[i]]) return a.score[priority[i]] > b.score[priority[i]];
        }
        return a.name > b.name;
    });

    for(const Student& s : students){
        cout << s.name << endl;
    }
}