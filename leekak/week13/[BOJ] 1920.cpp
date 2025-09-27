#include <iostream>
#include <algorithm>
#include <stdlib.h>

int compare (void *first, void *second)
{
    if (*(int*)first > *(int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else
        return 0;
}

using namespace std;
int main() {
    int N, M;
    cin >> N;
    int list[N];
    for(int i=0; i<N; i++) {
        cin >> list[i];
    }
    cin >> M;
    int arr[M];
    for(int i=0; i<M; i++) {
        cin >> arr[i];
    }

    sort(list, list+N);
    for(int i=0; i<M; i++) {
        cout << !!bsearch(&arr[i], list, N, sizeof(int), reinterpret_cast<int (*)(const void *, const void *)>(compare)) << "\n";
    }
    return 0;
}
