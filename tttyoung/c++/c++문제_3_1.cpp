#include <iostream>
using namespace std;

struct Point
{
	int xpos;
	int ypos;

	void MovePos(int x, int y)
	{
		xpos += x;
		ypos += y;
	}

	void AddPoint(const Point& a) // a의 값을 변경하지 않기 위채 const를 씀, 메모리 효율을 위해서 a의 값을 복사하여 쓰지 않고 참조를 통해 원본에 접근함
	{
		xpos += a.xpos;
		ypos += a.ypos;
	}

	void ShowPosition()
	{
		cout << "[" << xpos << ", " << ypos << "]" << endl;
	}
};

int main()
{
	Point pos1 = { 12, 4 };
	Point pos2 = { 20, 30 };

	pos1.MovePos(-7, 10);
	pos1.ShowPosition(); // [5, 14]출력

	pos1.AddPoint(pos2);
	pos1.ShowPosition(); // [25, 44] 출력
	return 0;
}
