#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


struct coordinate {
	int x, y;

};

//use gpt for simplifying if-else code (manhattan distance)
//맨해튼 거리를 이용한 좌표찾기
coordinate find(int time, const vector<coordinate>& p, const vector<int>& distance) {
    auto upper = upper_bound(distance.begin(), distance.end(), time);
    int under_index = upper - distance.begin() - 1;
    int sub_len = time - distance[under_index];
    coordinate result;

    int xdir = (p[under_index + 1].x > p[under_index].x) - (p[under_index + 1].x < p[under_index].x);
    int ydir = (p[under_index + 1].y > p[under_index].y) - (p[under_index + 1].y < p[under_index].y);

    result.x = p[under_index].x + xdir * sub_len;
    result.y = p[under_index].y + ydir * sub_len;

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
	points.push_back(points[0]);


	acc_distance.push_back(0);
	for (int i = 1; i <= k; i++) {
		int len = abs(points[i].x - points[i - 1].x) + abs(points[i].y - points[i - 1].y);
		acc_distance.push_back(acc_distance.back() + len);
	}
	int total_distance = acc_distance.back();
		
	struct coordinate first_c1 = points[0]; //c1의 좌표
	struct coordinate first_c2 = points[k / 2 - 1]; //c2의 좌표

	int t;
	cin >> t;

    //t초 뒤의 c1 c2 좌표의 누적거리 offset
	int time1 = t % total_distance;
	int time2 = (acc_distance[k / 2 - 1] - (t % total_distance) + total_distance) % total_distance;

	int crash_count = 0;
	if ((2 * t) >= (acc_distance[k / 2 - 1] % total_distance)) { //충돌할 경우
		crash_count = ((2 * t) - (acc_distance[k / 2 - 1] % total_distance)) / total_distance + 1; //충돌횟수
	}
	coordinate c1 = find(time1, points, acc_distance);
	coordinate c2 = find(time2, points, acc_distance);

	if (crash_count % 2 == 1) { //충돌횟수가 홀수라면 자리 swap
		swap(c1, c2);
	}
	cout << c1.x << " " << c1.y << "\n";
	cout << c2.x << " " << c2.y << "\n";
}