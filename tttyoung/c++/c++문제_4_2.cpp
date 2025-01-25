#include <iostream>
using namespace std;

class Point
{
private:
	int xpos, ypos;
public:
	void Init(int x, int y)
	{
		xpos = x;
		ypos = y;
	}
	void ShowPointInfo() const
	{
		cout << "[" << xpos << "," << ypos << "]" << endl;
	}
};

class Circle
{
private:
	Point center;
	int rad;
public:
	void Init(int x, int y, int r)
	{
		rad = r;
		center.Init(x, y);
	}
	void ShowCircleInfo()
	{
		cout << "radoius: " << rad << endl;
		center.ShowPointInfo();
	}
};

class Ring
{
private:
	Circle innercircle;
	Circle outercircle;
public:
	void Init(int x1, int y1, int r1, int x2, int y2, int r2)
	{
		innercircle.Init(x1, y1, r1);
		outercircle.Init(x2, y2, r2);
	}
	void ShowPointInfo()
	{
		cout << "Inner Cicle Info..." << endl;
		innercircle.ShowCircleInfo();
		cout << "Outter Cicle Info..." << endl;
		outercircle.ShowCircleInfo();
	}
};

int main()
{
	Ring ring;
	ring.Init(1, 1, 4, 2, 2, 9);
	ring.ShowPointInfo();
	return 0;
}
