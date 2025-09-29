    #include <iostream>
    #include <vector>
    #include <fstream>
    #include <cmath>
    #include <algorithm>
    #include <limits>

    using namespace std;

    struct num { //txt 파일 데이터 한줄의 struct
        int time_val;
        double coin_value;
    };

    struct Node {
        double min_val;
        double max_val;
    };

    //세그먼트 트리 채우기
    void build(vector<Node>& tree, vector<num>& data, int node, int start, int end) {
        //재귀 탈출조건
        if (start == end) {
            tree[node] = { data[start].coin_value, data[start].coin_value };
            return;
        }
        //왼쪽 오른쪽 구간을 나누어 재귀
        int mid = (start + end) / 2;
        build(tree, data, node * 2, start, mid);
        build(tree, data, node * 2 + 1, mid + 1, end);

        tree[node] = {min(tree[node * 2].min_val, tree[node * 2 + 1].min_val), max(tree[node * 2].max_val, tree[node * 2 + 1].max_val)};
    }

    //left, right 구간을 통해 segment tree에서 최대 최솟값 찾기
    Node query(vector<Node>& tree, int node, int start, int end, int left, int right) {
        //escape condition implemented with help of AI tools.
        if (right < start || end < left) {
            return { numeric_limits<double>::max(), numeric_limits<double>::lowest() };
        }

        if (left <= start && end <= right) {
            return tree[node]; 
        }
        //왼쪽 오른쪽 구간을 나누어 재귀
        int mid = (start + end) / 2;
        Node left_result = query(tree, node * 2, start, mid, left, right);
        Node right_result = query(tree, node * 2 + 1, mid+1, end, left, right);
        return { min(left_result.min_val, right_result.min_val), max(left_result.max_val, right_result.max_val) };
    }

    //time_val로 정렬되어있기 때문에 구간검색시에 사용하는 time을 index로 바꿔주는 작업
    int make_index(vector<num> &data, int time) {
        //help from AI for getting upperbound of struct
        auto upper = upper_bound(
            data.begin(),
            data.end(),
            time,
            [](int t, const num& n) {
                return t < n.time_val;
            }
        );

        int idx = (upper - data.begin()) - 1;
        return idx;
    }

    int main()	
    {	
        ios::sync_with_stdio(false); 
        cin.tie(nullptr);

        vector<num> data;
        ifstream fin("Pitcoin.txt");
        int N; //입력개수
        fin >> N;
        data.reserve(N); //vector에 공간 미리 할당
        num line_data;
        while (fin >> line_data.time_val >> line_data.coin_value) {
            data.emplace_back(line_data);
        }

        //tree벡터에 공간할당
        int height = (int)(ceil(log2(N)));
        vector<Node> tree(1 << (height + 1));

        build(tree, data, 1, 0, N - 1);

        int m;
        cin >> m;
        for (int i = 0; i < m; i++) {
            int tb, te;
            cin >> tb >> te;

            int left = make_index(data, tb);
            int right = make_index(data, te);

            Node result;
            result = query(tree, 1, 0, N - 1, left, right);
            cout << fixed;
            cout.precision(3); //소수점3번째 자리까지
            cout << result.min_val << " "<< result.max_val<<"\n";
        }
    }