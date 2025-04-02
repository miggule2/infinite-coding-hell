#include <iostream>

using namespace std;

class Foo {
private:
    int brain[2][500];
public:
    //CSEInint은 위치 + 1을 해당 위치에 저장함. ex)1에는 2, 2에는 3. 만약 500이 넘어갈 경우에는 숫자를 뒤집어 앞 3자리만 저장. 
    void CSEInit() {
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 500; ++j) {
                int num = i * 500 + j + 1;
                if (num >= 500) {
                    int res = 0, tmp = num;
                    while (tmp > 0) {
                        res = (res * 10) + (tmp % 10);
                        tmp /= 10;
                    }
                    while (res >= 1000) res /= 10;
                    brain[i][j] = res;
                }
                else brain[i][j] = num;
            }
        }
    };

    //Arm은 위치를 넣으면 해당 위치에 있는 value를 반환한다.
    int Arm(int loc) {
        return brain[loc / 500][loc % 500];
    };

    //Foot은 value를 넣으면 해당 위치를 반환한다. 만약 같은 값이 여러개 있을 경우에는 마지막에서 2번째의 위치를 반환한다.
    int Foot(int value) {
        int count = 0;
        int idx = -1;
        bool found = false;
        for (int i = 1; i >= 0; --i) {
            for (int j = 499; j >= 0; --j) {
                if (brain[i][j] == value) {
                    count += 1;
                    idx = i * 500 + j;
                    if (count == 2) {
                        found = true;
                        break;
                    }
                }
            }
            if (found) {
                break;
            }
        }
        if (idx == -1) return 500;
        else return idx;
    };

    void PRINT() {
        int result1 = 0, result2 = 0;
        for (int i = 0; i < 1000; ++i) {
            result1 = Arm(Foot(result1));
            result2 = Foot(Arm(result2));
        }
        cout << result1 << " " << result2 << endl;
    };
};

int main()
{
    Foo foo;
    foo.CSEInit();
    foo.PRINT();
}


