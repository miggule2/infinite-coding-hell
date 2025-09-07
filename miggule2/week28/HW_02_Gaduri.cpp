#define PI 3.14159265358979 

#include <iostream> 
#include <cmath> 

using namespace std;

// chat GPT : for code refactoring
// advising to group related variables together.
struct Point{ double x,y;};
struct SectorForm{ Point O; double r; double angle;};
struct Result{ double area; double round;};


inline double getSectorFormArea(const SectorForm& A){
    return 0.5*pow(A.r,2)*A.angle;
}

inline double getSectorFormRound(const SectorForm& A){
    return A.r*A.angle;
}

// chat gpt : for code refactoring
// I wrote the logic myself, and was advised to separate it into a function that only does the calculations.
Result solve(const SectorForm& A, const SectorForm& B){
    SectorForm big = (A.r > B.r) ? A : B; 
    SectorForm small = (A.r > B.r) ? B : A; 

    double d = sqrt(pow(A.O.x-B.O.x,2) + pow(A.O.y-B.O.y,2));
    double targentLen = sqrt((d*d) - pow(big.r-small.r,2));

    small.angle = 2*asin(targentLen/d);
    big.angle = 2*PI - small.angle;

    double area = (big.r + small.r) * targentLen + getSectorFormArea(small) + getSectorFormArea(big);
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


    