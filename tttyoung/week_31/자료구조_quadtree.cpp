#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

void img_to_qts(const vector<vector<int>>& image, int s, int r, int c) { //img to qts함수
    //재귀함수를 사용하여 쪼개진 조각에 대해 다시 출력 반복
	for (int i = r; i < r + s; i++) { 
		for (int j = c; j < c + s; j++) {
			if (image[i][j] != image[r][c]) {
				cout << "(";
				int newsize = s / 2;
				img_to_qts(image, newsize, r, c + newsize); 
				img_to_qts(image, newsize, r, c); 
				img_to_qts(image, newsize, r + newsize, c); 
				img_to_qts(image, newsize, r + newsize, c + newsize); 
				cout << ")";
				return;
			}
		}
	}
	cout << image[r][c];
}

void fill(vector<vector<int>>& image, int r, int c, int s, int value) {
    //주어진 크기에 대한 image이중벡터 채워주기
	for (int i = r; i < r + s; i++) {
		for (int j = c; j < c + s; j++) {
			image[i][j] = value;
		}
	}
}

void qts_to_img(const string& qts_str, int& index, vector<vector<int>>& image, int r, int c, int s)
{ //qts to image함수
	char curr = qts_str[index]; //char로 하나씩 넣어주기
	index++; 

	if (curr == '(') { // 여는 괄호 입력시 재귀
		int newsize = s / 2;
		qts_to_img(qts_str, index, image, r, c + newsize, newsize); 
		qts_to_img(qts_str, index, image, r, c, newsize);           
		qts_to_img(qts_str, index, image, r + newsize, c, newsize); 
		qts_to_img(qts_str, index, image, r + newsize, c + newsize, newsize); 

		index++; 
	}
	else { // 닫는괄호 입력시 값 채워주기
		int value = curr - '0';
		fill(image, r, c, s, value);
	}
}

int main()
{
    int k;
    string command;
    cin >> k >> command;
    if (command == "IMG") {
		vector<vector<int>> image(pow(2, k), vector<int>(pow(2, k)));
		for (int i = 0; i < pow(2, k); i++) {
			string row;
			cin >> row;
			for (int j = 0; j < pow(2, k); j++) {
				image[i][j] = row[j] - '0';
			}
		}
		img_to_qts(image, pow(2, k), 0, 0);
	}
	else if (command == "QTS") {
		string qts;
		cin >> qts;
		vector<vector<int>> image(pow(2, k), vector<int>(pow(2, k)));
		
		int index = 0;
		qts_to_img(qts, index, image, 0, 0, pow(2, k));
		for (int i = 0; i < pow(2, k); i++) {
			for (int j = 0; j < pow(2, k); j++) {
				cout << image[i][j];
			}
			cout << endl;
		}
	}
}
