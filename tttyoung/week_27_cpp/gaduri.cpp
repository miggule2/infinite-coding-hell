#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>
using namespace std;

int main()
{
    int x1, y1, r1;
    int x2, y2, r2;

    cin >> x1 >> y1 >> r1;
    cin >> x2 >> y2 >> r2;
    int dx = x2 - x1;
    int dy = y2 - y1;
    double d = sqrt(dx * dx + dy * dy);
    double l = sqrt(d * d - pow(r2 - r1, 2));
    double rad = asin(l / d);
    int min_r = min(r1, r2); //반지름 크기에 따라 결과 계산시 곱해주는 각도가 달라지기 때문에 반지름 대소비교
    int max_r = max(r1, r2);


    double total_length = 2 * l + 2 * min_r * rad + 2 * max_r * (M_PI - rad);
    double total_area = l * (r1 + r2) + pow(min_r, 2) * rad + pow(max_r, 2) * (M_PI - rad);

    double result_length = floor(total_length); //floor를 이용해 정수처리
    double result_area = floor(total_area);
    cout << (long long)result_area << " " << (long long)result_length;
}

