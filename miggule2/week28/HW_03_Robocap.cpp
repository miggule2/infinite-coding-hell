#include <iostream>
#include <vector>

using namespace std;

struct Point{
    int x;
    int y;
};

struct Time{
    int time;
    int way;
};

Time calculateWayToGo(Point& point1, Point& point2){
    int time, way;

    if(point1.x == point2.x) return {abs(point1.y - point2.y), point1.y - point2.y > 0 ? 0 : 1};
    else return {abs(point1.x - point2.x), point1.x - point2.x > 0 ? 2 : 3};

}

int main(){
    int n;
    cin >> n;

    vector<Point> points;
    vector<Time> wayToGo;
    Point prev = {0,0};
    int totalTime = 0;
    for(int i = 0; i < n; i++){
        int x, y;
        cin >> x >> y;
        points.push_back({x,y});

        if(i == 0){
            wayToGo.push_back({0,-1});
        } else{
            Time toGo = calculateWayToGo(points[i], prev);
            totalTime += toGo.time;
            wayToGo.push_back({totalTime,toGo.way});
        }
        prev = {x,y};
    }
    Time toGo = calculateWayToGo(points[0],points[n-1]);
    totalTime += toGo.time;
    wayToGo.push_back({totalTime,toGo.way});

    for(int i = 0; i < 5; i++){
        int t;
        cin >> t;
        t %= totalTime;
        int prevTime = 0;
        int x, y;
        for(int j = 0; j < wayToGo.size(); j++){
            int time = wayToGo[j].time;
            if(time == t) {
                x = points[j].x;
                y = points[j].y;
                break;
            }
            else if(t > prevTime && t < time) {
                x = points[j-1].x;
                y = points[j-1].y;

                int way = wayToGo[j].way;
                int calTime = t - prevTime;
                if(way == 0 || way == 1) y = way == 0 ? y+calTime : y-calTime;
                else x = way == 2 ? x+calTime : x-calTime;
                break;
            }
            prevTime = wayToGo[j].time;
        }
        cout << x << " " << y << endl;
    }
}