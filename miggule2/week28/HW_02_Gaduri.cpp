#define PI 3.14159265358979 

#include <iostream> 
#include <cmath> 

using namespace std;

// chat GPT : for code refactoring
// advising to group related variables together.
struct Point{ double x,y;}; // 좌표를 위한 구조체
struct SectorForm{ Point O; double r; double angle;}; // 부채콜을 나타내기 위한 구조체
struct Result{ double area; double round;};

// 부채꼴 넓이 구하는 함수
inline double getSectorFormArea(const SectorForm& A){
    return 0.5*pow(A.r,2)*A.angle;
}

// 부채꼴 호의 길이 구하는 함수
inline double getSectorFormRound(const SectorForm& A){
    return A.r*A.angle;
}

// chat gpt : for code refactoring
// I wrote the logic myself, and was advised to separate it into a function that only does the calculations.
Result solve(const SectorForm& A, const SectorForm& B){
    SectorForm big = (A.r > B.r) ? A : B; 
    SectorForm small = (A.r > B.r) ? B : A; 

    // 원의 중심 간의 거리
    double d = sqrt(pow(A.O.x-B.O.x,2) + pow(A.O.y-B.O.y,2));
    // 접선의 길이
    double targentLen = sqrt((d*d) - pow(big.r-small.r,2));

    // 필요한 부채꼴의 중심각
    small.angle = 2*asin(targentLen/d);
    big.angle = 2*PI - small.angle;

    // 접선으로 생긴 사다리꼴 + 두 부채꼴 넓이
    double area = (big.r + small.r) * targentLen + getSectorFormArea(small) + getSectorFormArea(big);
    // 접선 + 두 부채꼴의 호의 길이
    double round = 2*targentLen + getSectorFormRound(small) + getSectorFormRound(big);

    return {area,round};
}

int main(){ 
    SectorForm A, B;
    
    cin >> A.O.x >> A.O.y >> A.r; 
    cin >> B.O.x >> B.O.y >> B.r; 
    
    Result result = solve(A,B);

    cout << floor(result.area) << " " << floor(result.round);

    return 0;
}


    