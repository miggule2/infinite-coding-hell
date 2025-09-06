#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

#define INT_MAX 0x8FFFFFFF

int recursion(int *dp, int level){
    if(level == 1) return 0; // 1인 경우(기저 조건) 특수하게 0을 리턴 
    if(level < 1) return INT_MAX; // 조건 보다 작은 수는 min 함수에서 제외되도록 정수 최댓값 리턴
    if(dp[level] != 0) return dp[level]; // 메모이제이션된 수를 사용

    // 로직 설명
    // 1. 최소 계산 조건이기 때문에 recursion(level/3,level/2,level-1) 값들 중 최솟값을 dp값으로 넣음(메모이제이션)
    // 2. 그 값을 그대로 념겨주는 걸 반복하여 dp[1]까지 내려감(메모이제이션에 걸리면 그 전에 끝남)
    // 3. 그럼 최종적으로 dp[level]에 최솟값이 들어가게 됨.
    if(level%6 == 0) return dp[level] = 1+min(min(recursion(dp,level/2), recursion(dp,level/3)), recursion(dp,level-1));
    else if(level%3 == 0) return dp[level] = 1+min(recursion(dp,level/3), recursion(dp,level-1));
    else if(level%2 == 0) return dp[level] = 1+min(recursion(dp,level/2), recursion(dp,level-1));
    else return dp[level] = 1+recursion(dp,level-1);
}

int main(){
    int n;
    cin >> n;

    int dp[n+1];
    memset(dp, 0, sizeof(dp));
    dp[1]=0; // 초기값 설정

    recursion(dp,n);

    cout << dp[n] << endl;
}