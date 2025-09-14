#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class WaitingLine{
private :
    vector<vector<int>> waiting;
    int inner_vector_size;
public :
    WaitingLine(int size) : inner_vector_size(size){};
    void add_element(int num);
    void delete_element(int num);
    void print_first_elements();
};

void WaitingLine::add_element(int num) {
    if(waiting.empty()) {
        waiting.emplace_back();
        waiting[0].push_back(num);
        return;
    }

    /* try
     * index = 0;
     * bool isEnd = true;
     * for(int i = 0; i < waiting.size()-1;i++){
     *      if(waiting[0][0] > num){
     *          index = 0;
     *          isEnd = false;
     *          break;
     *
     *      if(waiting[i][0] > num){
     *          index = i-1;
     *          isEnd = false;
     *          break;
     *      }
     * if(isEnd) index = waiting.size()-1;
     */
    // gemini
    // Attempts to find the index by comparing it to the number behind it. However, exceptions keep occurring at the beginning and end, so I need help from Gemini.
    int index = 0;
    for(int i = 0; i < waiting.size(); i++){
        if(waiting[i][0] <= num){
            index = i;
        } else break;
    }
    //

    auto it = lower_bound(waiting[index].begin(), waiting[index].end(),num);
    waiting[index].insert(it,num);

    if(waiting[index].size() == inner_vector_size){
        waiting.insert(waiting.begin()+index+1, vector<int>(waiting[index].begin()+inner_vector_size/2,waiting[index].begin()+inner_vector_size));
        waiting[index].erase(waiting[index].begin()+inner_vector_size/2,waiting[index].begin()+inner_vector_size);
    }
}

void WaitingLine::delete_element(int num) {
    if(waiting.empty()) return;

    int index = 0;
    for(int i = 0; i < waiting.size(); i++){
        if(waiting[i][0] <= num){
            index = i;
        } else break;
    }

    auto it = find(waiting[index].begin(), waiting[index].end(),num);
    if(it == waiting[index].end()) return;
    else waiting[index].erase(it);

    if(waiting[index].empty()) waiting.erase(waiting.begin()+index);
}

void WaitingLine::print_first_elements() {
    for(vector<int> wait : waiting){
        cout << wait[0] << endl;
    }
}

int main(){
    int n, k;
    cin >> n >> k;

    auto* waitingLine = new WaitingLine(2*k);
    for(int i = 0; i < n; i++){
        string op;
        int num;

        cin >> op >> num;
        if(op == "+") waitingLine->add_element(num);
        else waitingLine->delete_element(num);
    }

    waitingLine->print_first_elements();
    delete waitingLine;
}