#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct person { //나이, 이름 담는 struct
    int age;
    string name;
};

int main()
{
    int n;
    cin >> n;
    vector<person> people;
    for (int i = 0; i < n; i++) { //people 구조체벡터에 입력받은 나이, 이름 push_back
        person p;
        cin >> p.age >> p.name;
        people.push_back(p);
    }
    stable_sort(people.begin(), people.end(), [&](const person& a, const person& b) { //stable_sort로 정렬순서 지킴
        return a.age < b.age; //나이순서로 정렬
        });
    for (int i = 0; i < n; i++) cout << people[i].age << " " << people[i].name<<"\n";
}
