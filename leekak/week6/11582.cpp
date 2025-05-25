#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& arr, int left, int mid, int right, int N, int k) {
    if(right-left+1 > N/k) return;
    //병합할 길이가 N/k보다 커지면 종료!
    //그래야 k에 따른 현재 단계가 나옴
    //여기 빼고는 그냥 병합정렬임
    vector<int> result(right-left+1);
    int a = left;
    int b = mid + 1;
    int c = 0;

    while(a<=mid && b<=right) {
        if(arr[a] <= arr[b]) {
            result[c] = arr[a];
            a++;
        } else {
            result[c] = arr[b];
            b++;
        }
        c++;
    }
    if(a>mid) {
        while(b<=right) {
            result[c]=arr[b];
            c++;
            b++;
        }
    } else {
        while(a<=mid) {
            result[c]=arr[a];
            a++;
            c++;
        }
    }
    for(int i=left, j=0; i<=right; i++, j++) {
        arr[i] = result[j];
    }
}

void merge_sort(vector<int>& arr, int left, int right, int N, int k) {
    if(left<right) {
        int mid = (left+right)/2;
        merge_sort(arr, left, mid, N, k);
        merge_sort(arr, mid+1, right, N, k);
        merge(arr, left, mid, right, N, k);
    }
}

int main() {
    int N, k;
    cin >> N;
    vector<int> score(N);
    for(int i=0; i<N; i++) {
        cin >> score[i];
    }
    cin >> k;
    merge_sort(score, 0, N-1 ,N, k);
    for(int i=0; i<N; i++) {
        cout << score[i] << " ";
    }

    return 0;
}
