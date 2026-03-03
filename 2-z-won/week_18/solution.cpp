#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

#define HM 100000000

unsigned long PNUhash(unsigned long long x, int salt) {
    x = x + salt;
    x = (x ^ (x >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    x = (x ^ (x >> 27)) * UINT64_C(0x94d049bb133111eb);
    x = x ^ (x >> 31);
    return x % HM;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, salt;
    if (!(cin >> N >> salt)) return 0;

    int valid_cnt = 0;
    int invalid_cnt = 0;
    int used_cnt = 0;

    char code[21]; 
    unordered_set<string> seen_valid;
    seen_valid.reserve(N); 

    for (int i = 0; i < N; i++) {
        cin >> code;
        
        unsigned long long K = 0;
        // d1~d4
        K = K * 10 + (code[2] - '0');
        K = K * 10 + (code[3] - '0');
        K = K * 10 + (code[4] - '0');
        K = K * 10 + (code[5] - '0');
        // d5~d8
        K = K * 10 + (code[8] - '0');
        K = K * 10 + (code[9] - '0');
        K = K * 10 + (code[10] - '0');
        K = K * 10 + (code[11] - '0');
        // d9~d12
        K = K * 10 + (code[14] - '0');
        K = K * 10 + (code[15] - '0');
        K = K * 10 + (code[16] - '0');
        K = K * 10 + (code[17] - '0');

        unsigned long hash_val = PNUhash(K, salt);
        
        // H7, H8 (code[18], code[19]) - 1의 자리, 10의 자리
        if ((hash_val % 10) != (code[19] - '0')) { invalid_cnt++; continue; }
        hash_val /= 10;
        if ((hash_val % 10) != (code[18] - '0')) { invalid_cnt++; continue; }
        hash_val /= 10;

        // H5, H6 (code[12], code[13])
        if ((hash_val % 10) != (code[13] - '0')) { invalid_cnt++; continue; }
        hash_val /= 10;
        if ((hash_val % 10) != (code[12] - '0')) { invalid_cnt++; continue; }
        hash_val /= 10;

        // H3, H4 (code[6], code[7])
        if ((hash_val % 10) != (code[7] - '0')) { invalid_cnt++; continue; }
        hash_val /= 10;
        if ((hash_val % 10) != (code[6] - '0')) { invalid_cnt++; continue; }
        hash_val /= 10;

        // H1, H2 (code[0], code[1])
        if ((hash_val % 10) != (code[1] - '0')) { invalid_cnt++; continue; }
        hash_val /= 10;
        if ((hash_val % 10) != (code[0] - '0')) { invalid_cnt++; continue; }
        
        string s_code = code;
        if (seen_valid.find(s_code) != seen_valid.end()) {
            used_cnt++;
        } else {
            valid_cnt++;
            seen_valid.insert(s_code);
        }
    }

    cout << valid_cnt << "\n";
    cout << invalid_cnt << "\n";
    cout << used_cnt << "\n";

    return 0;
}