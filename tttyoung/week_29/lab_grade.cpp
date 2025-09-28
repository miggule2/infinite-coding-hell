#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <algorithm>

using namespace std;

//이름, 정렬정보 담는 struct
struct Student {
    string name;
    vector<int> sorting_standard;

};
//기준별 점수 만드는 함수
vector<int> make_standard(vector<int>& grades) {
    vector<int> s;
    int count = grades.size();
    int total = accumulate(grades.begin(), grades.end(), 0);
    int minx = *min_element(grades.begin(), grades.end());
    int maxx = *max_element(grades.begin(), grades.end());
    int count_100 = count_if(grades.begin(), grades.end(), [](int c) {return c == 100; });
    s = { count, total, minx, maxx, count_100 };
    return s;
}

int main()
{
    int N, k;
    cin >> N >> k;

    vector<int> sorting(5); //정렬순서 입력받기
    for (int i = 0; i < 5; i++) cin >> sorting[i];

    vector<Student> students(N); //학생정보(이름, 기준별 점수) 담는 벡터
    for (int i = 0; i < N; i++) {
        cin >> students[i].name; //이름 입력
        vector <int> grades; //원점수 벡터
        for (int j = 0; j < k; j++) { //0이 아닌 원점수만 벡터에 저장
            int grade;
            cin >> grade;
            if (grade != 0)
                grades.push_back(grade);
        }
        students[i].sorting_standard = make_standard(grades);
    }
    //점수별 정렬, 만약 점수가 같다면 이름 사전순 정렬
    sort(students.begin(), students.end(), [&](const Student& a, const Student& b) {
        for (int i = 0; i < 5; i++) { //for문을 돌리면서 정렬기준을 계속 넘김
            if (a.sorting_standard[sorting[i] - 1] != b.sorting_standard[sorting[i] - 1])
                return a.sorting_standard[sorting[i] - 1] > b.sorting_standard[sorting[i] - 1];
        }
        return a.name < b.name;
        });

    for (const auto& student : students) {
        cout << student.name << "\n";
    }
}

