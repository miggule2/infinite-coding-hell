#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int T;
    cin >> T;
    while(T--) {
        int x1, y1, r1, x2, y2, r2;
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        if((x1 == x2) && (y1 == y2)) {
            if(r1 == r2) cout << -1;
            else cout << 0;
        } else {
            int sum = r1 + r2;
            int dif = abs(r2-r1);
            double dis = sqrt(pow(x2-x1, 2)+pow(y2-y1, 2));
            if((dis > dif) && (dis < sum))
                cout << 2;
            else if((dis == sum) || (dis == dif))
                cout << 1;
            else if((dis > sum) || (dis < dif))
                cout << 0;
        }
        cout << "\n";
    }
    return 0;
}
