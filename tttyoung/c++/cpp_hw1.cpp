#include <iostream> 
#include <string>

using namespace std;

class cseMAP {
private:
	int map[3][3];
	int _initialPlace;
	int _pathValue;
	// Declare additional member variables if you need them 
public:
	cseMAP() { }

	cseMAP(int initialPlace) {
		_initialPlace = initialPlace;
	}
	void findPathValue(string path) {
		int map[3][3] = {
			{1, 2, 3},
			{4, 5, 6},
			{7, 8, 9}
		};
		int x = (_initialPlace - 1) / 3; 
		int y = (_initialPlace - 1) % 3;
		_pathValue = map[x][y];

		for (char move : path) {
			if (move == '1') {
				if (y == 0) {
					y = 2;
				}
				else {
					y--;
				}
			}
			else if (move == '2') {
				if (y == 2) {
					y = 0;
				}
				else {
					y++;
				}
			}
			else if (move == '3') {
				if (x == 0) {
					x = 2;
				}
				else {
					x--;
				}
			}
			else if (move == '4') {
				if (x == 2) {
					x = 0;
				}
				else {
					x++;
				}
			}
			_pathValue += map[x][y];
		}
	}

	int getPathValue() {
		return _pathValue;
	}
};

int main(void) {
	cseMAP mapSolution1(5), mapSolution2(5), mapSolution3(5);

	string path1 = 
		"333342141211313444411113334211324222144331122344223124413243411321333122222113122414242234421442123324424432221312122421224331332413432334314234321114343234442142321412323231131222324411342331223132312444312214321413214313232413241141441412111311224221143324413423432143243222234422314433312231334313"; 
	string path2 = 
		"113411123144311114113111121333224334212221141111141314321423323334212321323444232312224123234442444222443314441214414424314111432214322134444423424333242212232342114422431234411213412214142421343322444434123224141111231311111214334142333223231324221323343113233431242222234332314321313343113232413113"; 

	mapSolution1.findPathValue(path1);
	mapSolution2.findPathValue(path2);
	cout << "Path1 Value: " << mapSolution1.getPathValue() << endl;
	cout << "Path2 Value: " << mapSolution2.getPathValue() << endl;
	return 0;
}