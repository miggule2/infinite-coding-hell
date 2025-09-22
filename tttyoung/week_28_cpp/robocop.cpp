//맨해튼거리 공부해보기
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct coordinate { //좌표 정보 담을 구조체
    int x;
    int y;
};

coordinate find(int time, const vector<coordinate>& p, const vector<int>& distance) {//coordinate구조체를 반환형으로 하는 함수
    auto upper = upper_bound(distance.begin(), distance.end(), time); 
    int under_index = upper - distance.begin() - 1; //시간보다 작거나 같은 좌표의 index
    int sub_len = time - distance[under_index]; //좌표와 시간의 차이
    coordinate result;

    if (p[under_index].x == p[under_index + 1].x) { //x좌표 같고 y좌표 다를때 -> y좌표 변화시켜줘야함
        if (p[under_index].y > p[under_index + 1].y) {
            result.x = p[under_index].x;
            result.y = p[under_index].y - sub_len;
        }
        else {
            result.x = p[under_index].x;
            result.y = p[under_index].y + sub_len;
        }
    }
    else { // x좌표 다르고 y좌표 같을때
        if (p[under_index].x > p[under_index + 1].x) {
            result.y = p[under_index].y;
            result.x = p[under_index].x - sub_len;
        }
        else {
            result.y = p[under_index].y;
            result.x = p[under_index].x + sub_len;
        }
    }
    return result;
}

int main()
{
    int k;
    cin >> k;
    vector<coordinate> points;
    vector<int> acc_distance;

    for (int i = 0; i < k; i++) {
        coordinate point;
        cin >> point.x >> point.y;
        points.push_back(point);
    }
    points.push_back(points[0]); //좌표벡터 마지막에 처음좌표를 추가 -> 전체길이 구할때 사용

    acc_distance.push_back(0); //좌표벡터와 index를 맞춰주기 위해 해당 index의 좌표에 도달하기까지의 누적거리를 담는 벡터
    for (int i = 1; i <= k; i++) {
        int len = abs(points[i].x - points[i - 1].x) + abs(points[i].y - points[i - 1].y);
        acc_distance.push_back(acc_distance.back() + len);
    }
    int total_distance = acc_distance.back();
    vector<int> finding_time;//시간을 전체길이로 나눠줌
    for (int i = 0; i < 5; i++) {
        int time;
        cin >> time;
        time = time % total_distance;
        finding_time.push_back(time); 
    }
    for (int t : finding_time) {
        coordinate answer = find(t, points, acc_distance);
        cout << answer.x << " " << answer.y << "\n";
    }
}

