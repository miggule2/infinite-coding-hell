#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

struct Point{
    int x;
    int y;
};

// 로봇의 위치를 찾는 함수
Point findPosition(vector<Point>& arr, int index, int total_distance, int t, bool isRound){
    int size = arr.size();
    int time = t % total_distance;
    int i = index;
    while(true){
        Point start = arr[i], end;
        if(isRound){
            end = arr[(i+1)%size];
        } else{
            end = arr[((i-1)%size + size)%size]; // gemini : Negative number processing modulo operation
        }


        // gemini : The solution of subtracting the length of the corresponding location from the total length was thought of by Robocop, but I received advice from gemini to solve the solution of calculating the difference from the next coordinate each time for the length as an absolute value and for the direction.
        int temp_length = abs(start.x-end.x) + abs(start.y-end.y);
        if(time < temp_length) {
            int direction;
            if(start.y == end.y){
                direction = end.x - start.x > 0 ? 1 : -1; // gemini
                return {start.x+direction*(int)time, start.y};
            } else{
                direction = end.y - start.y > 0 ? 1 : -1; // gemini
                return{start.x, start.y+direction*(int)time};
            }
        }

        time -= temp_length;

        if(isRound) i = (i+1)%size;
        else i = (i-1+size)%size; // gemini : Negative number processing modulo operation
    }

    return arr[0];
}

// pass-through(두 로봇의 이동 경로를 바꾸지 않고 위치를 구한 다음, 충돌 횟수에 따라 위치를 바꿔줌 -> 충돌을 한 순간 원래 c1의 경로를 c2가 / c2의 경로를 c1이 따라 이동함.)
int main(){
    int n;
    cin >> n;
    vector<Point> arr;

    for(int i = 0; i< n; i++){
        int x, y;
        cin >> x >> y;
        arr.push_back({x,y});
    }

    int result_t;
    cin >> result_t;

    // 전체 길이와 c1_c2간의 거리를 측정
    int total_distance= 0;
    double c1_c2_distance = 0;
    for(int i = 0; i < n; i++){
        Point current = arr[i];
        Point next = arr[(i+1)%n]; // gemini : Connect from the last vertex to the first vertex
        int distance = abs(current.x - next.x) + abs(current.y - next.y);
        if(i < (n/2)-1){
            c1_c2_distance += distance;
        }
        total_distance += distance;
    }

    // 충돌 횟수 카운팅을 위한 로직
    int t = 0;
    int collision_count = 0;
    int first_collision = 0;
    // 시간을 1씩 늘려가며 result_t가 될 때까지 늘리면서 충돌 횟수 카운팅
    while(t <= result_t){
        // 처음 충돌 시간 구하기
        // 2*t(c1+c2가 이동한 시간)이 c1_c2_distance를 넘어가는 순간 충돌
        if(first_collision == 0 && 2*t >= c1_c2_distance){
            first_collision = 2*t;
            collision_count++;
        }
        
        // 이후 충돌 시간 구하기
        // 2*t(c1+c2가 이동한 시간)이 처음 충돌 이후 충돌간격 * 충돌카운팅을 한 만큼 넘어가는 순간 충돌
        if(first_collision != 0 && 2*t >= first_collision + collision_count*total_distance){
            collision_count++;
        }
        t++;
    }

    Point c1_Position, c2_Position;
    c1_Position = findPosition(arr,0,total_distance,result_t,true);
    c2_Position = findPosition(arr,n/2-1,total_distance, result_t, false);
    if(collision_count%2 == 1){
        Point temp = c1_Position;
        c1_Position = c2_Position;
        c2_Position = temp;
    }

    cout << c1_Position.x << " " << c1_Position.y << endl;
    cout << c2_Position.x << " " << c2_Position.y << endl;
}