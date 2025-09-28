#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

// using gemini : No need to create separate maximum and minimum segment trees.
struct Node{
    double max_price;
    double min_price;
};
//

vector<int> timeArr;
vector<double> priceArr;
vector<Node> segTree;

void buildSegTree(int start, int end, int index){
    if(start == end) {
        segTree[index] = {priceArr[start], priceArr[start]};
        return;
    }

    int mid = (start+end)/2;
    buildSegTree(start, mid, index*2+1);
    buildSegTree(mid+1, end, index*2+2);

    segTree[index].min_price = min(segTree[index*2+1].min_price, segTree[index*2+2].min_price);
    segTree[index].max_price = max(segTree[index*2+1].max_price, segTree[index*2+2].max_price);
}

double getMin(int start, int end, int nowStart, int nowEnd, int index){
    if(nowEnd < start || nowStart > end){
        return 10000000;
    }

    if(nowStart >= start && nowEnd <= end){
        return segTree[index].min_price;
    }

    int mid = (nowStart+nowEnd)/2;
    return min(getMin(start,end,nowStart,mid,index*2+1), getMin(start,end,mid+1,nowEnd,index*2+2));
}

double getMax(int start, int end, int nowStart, int nowEnd, int index){
    if(nowEnd < start || nowStart > end){
        return -1;
    }

    if(nowStart >= start && nowEnd <= end){
        return segTree[index].max_price;
    }

    int mid = (nowStart+nowEnd)/2;
    return max(getMax(start,end,nowStart,mid,index*2+1), getMax(start,end,mid+1,nowEnd,index*2+2));
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    ifstream pitcoin("Pitcoin.txt");
    int data_size;
    pitcoin >> data_size;
    int time;
    double price;

    while(pitcoin >> time >> price){
        timeArr.push_back(time);
        priceArr.push_back(price);
    }
    // using gemini : To access vectors directly in a segment tree, you must specify their size in advance.
    segTree.resize(8*data_size);

    buildSegTree(0,data_size-1,0);

    int length;
    cin >> length;

    for(int i = 0; i < length; i++){
        int startTime, endTime;
        cin >> startTime >> endTime;

        // using gemini : Originally, I tried to handle it as "lower_bound", but there was a problem where the end value was not handled properly. So, I handled it as "upper_bound - 1".
        int start = upper_bound(timeArr.begin(), timeArr.end(), startTime) - timeArr.begin() -1;
        int end = upper_bound(timeArr.begin(), timeArr.end(), endTime) - timeArr.begin() - 1;
        //

        cout << fixed << setprecision(3);
        cout << getMin(start,end,0,data_size-1,0) << " " << getMax(start,end,0,data_size-1,0) << "\n";
    }
}